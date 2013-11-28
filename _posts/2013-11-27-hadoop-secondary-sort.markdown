---
layout: post
title: Hadoop 二次排序 (secondary sort)
---

### 二次排序原理

很多时候我们希望 reducer 接受到的 value 是按某种方式排序的，比如你有两种 value，希望第一种 value 出现在第二种 value 的前面，这时你就需要二次排序 (secondary sort)。

(K, V) 集合从 mapper 产生到 reducer 开始处理之前，依次经过 partition -> sort -> group。partition 将 (K, V) 集合按某种方式（比如按 hash value）分给不同的 reducer（注意：有相同 K 的 (K, V) 一定去同一个 reducer，但同一个 reducer 会接收包含不同 K 的 (K, V)），然后 reducer 对收到的所有 (K, V) 按 K 排序，并将有相同 K 的 (K, V) group 起来交给你写的 reducer 函数处理。

这里面共涉及 3 个类（类名我随便写的）：

* Partitioner：这个类用于在 partition 的过程中决定一个 (K, V) 去哪个 reducer
* KeyComparator：这个类用于在 sort 的过程中比较两个 K 的大小
* GroupingComparator：这个类用于在 group 的过程中比较两个 K 的大小

为了实现二次排序，需要自己定义一个 composite key，composite key 包含 natrual key 和一个附加 key。partition 的时候根据 natrual key partition，sort 的时候根据 composite key sort，group 的时候又根据 natrual key group。这样就实现了 secondary sort。

因此，实现二次排序需要作如下修改：

* 添加一个 CompositeKey class，并针对这个类定义上面给出的 3 个类
* 修改 JobConf

### 代码示例

下面定义了一个包含 String, String 的 CompositeKey。这个 CompositeKey 实现 WritableComparable 接口，该接口定义了 3 个函数：

{% highlight java %}
public void readFields(DataInput in) throws IOException {}
public void write(DataOutput out) throws IOException {}
public int compareTo(CompositeKey o) {}
{% endhighlight %}

类实现如下：

{% highlight java %}
import java.io.IOException;
import java.io.DataInput;
import java.io.DataOutput;

import org.apache.hadoop.io.WritableComparable;
import org.apache.hadoop.io.WritableComparator;
import org.apache.hadoop.io.WritableUtils;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.mapred.Partitioner;

public class StringCompositeKey implements WritableComparable<StringCompositeKey> {
    private String k1; /* the natrual key */
    private String k2;

    public StringCompositeKey()
    {   
        this.k1 = ""; 
        this.k2 = ""; 
    }   

    public StringCompositeKey(String k1, String k2) 
    {   
        this.k1 = k1; 
        this.k2 = k2; 
    }   

    public String getK1()
    {   
        return k1; 
    }

    public String getK2()
    {
        return k2;
    }
    
    @Override
    public void readFields(DataInput in) throws IOException
    {   
        k1 = WritableUtils.readString(in);
        k2 = WritableUtils.readString(in);
    }

    @Override
    public void write(DataOutput out) throws IOException
    {
        WritableUtils.writeString(out, k1);
        WritableUtils.writeString(out, k2);
    } 
    
    @Override
    public int compareTo(StringCompositeKey o)
    {   
        int result = k1.compareTo(o.k1);
        if (result != 0) {
            return result;
        }
        return k2.compareTo(o.k2);
    }
    
    public static class NaturalKeyPartitioner<V>
        implements Partitioner<StringCompositeKey, V> {

        public void configure(JobConf job) {}

        @Override
        public int getPartition(StringCompositeKey key, V val,
                                int numPartitions)
        {
            return key.getK1().hashCode() % numPartitions;
        }
    }

    public static class CompositeKeyComparator 
        extends WritableComparator {

        protected CompositeKeyComparator() {
            super(StringCompositeKey.class, true);
        }
        
        @Override
        public int compare(WritableComparable w1, WritableComparable w2) {
            StringCompositeKey ck1 = (StringCompositeKey)w1;
            StringCompositeKey ck2 = (StringCompositeKey)w2;
            return ck1.compareTo(ck2);
        }
    }

    public static class NaturalKeyGroupingComparator
        extends WritableComparator {

        protected NaturalKeyGroupingComparator() {
            super(StringCompositeKey.class, true);
        }
        
        @Override
        public int compare(WritableComparable w1, WritableComparable w2) {
            StringCompositeKey ck1 = (StringCompositeKey)w1;
            StringCompositeKey ck2 = (StringCompositeKey)w2;
            return ck1.getK1().compareTo(ck2.getK2());
        }
    }
}
{% endhighlight %}

相应的 JobConf 中的修改包括：

{% highlight java %}
public static void
main(String[] args) throws Exception
{
    ... ...

    job.setMapOutputKeyClass(StringCompositeKey.class);

    job.setPartitionerClass(NaturalKeyPartitioner.class);
    job.setOutputValueGroupingComparator(NaturalKeyGroupingComparator.class);
    job.setOutputKeyComparatorClass(CompositeKeyComparator.class);

    ... ...
}
{% endhighlight %}

