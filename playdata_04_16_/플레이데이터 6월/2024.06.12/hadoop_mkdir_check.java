package com.example;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;

public class encore {
    public static void main(String[] args) throws URISyntaxException, IOException  {
         String namenode = "hdfs://ip:port"; // 실제 NameNode 주소로 변경
 
 
         Configuration configuration = new Configuration();
         configuration.addResource(new Path("/home/hadoop/hadoop/etc/hadoop/core-site.xml"));
         configuration.addResource(new Path("/home/hadoop/hadoop/etc/hadoop/hdfs-site.xml"));
 
 
         configuration.set("fs.defaultFS", namenode);
         configuration.set("fs.hdfs.impl", org.apache.hadoop.hdfs.DistributedFileSystem.class.getName());
 
 
         FileSystem fs = FileSystem.get(new URI(namenode), configuration);
         if (!fs.exists(new Path("/mort"))){
            fs.mkdirs(new Path(("/mort")));
         }
 
  FileStatus[] fileStatuses = fs.listStatus(new Path("/")); // HDFS 루트 디렉토리
         for (FileStatus status : fileStatuses) {
             System.out.printf("%-10s %-10s %-20s %-20s%n", 
                 (status.isDirectory() ? "d" : "-"),  
                 status.getPermission(),              
                 status.getOwner(),                   
                 status.getPath().getName()           
             );
         }
         
 
         fs.close();
 
     }

 }
 