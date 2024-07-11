package com.springboot.advanced_jpa.data.repository;




import com.springboot.advanced_jpa.data.entity.Product;


import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;
import org.springframework.data.domain.Sort.Order;


import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;


@SpringBootTest
public class ProductRepositoryTest {


    @Autowired
    ProductRepository productRepository;
   
    @Test
    void ProductTest(){
        Product product1 = new Product();
        product1.setName("펜");
        product1.setPrice(1000);
        product1.setStock(100);
        product1.setCreatedAt(LocalDateTime.now());
        product1.setUpdatedAt(LocalDateTime.now());
        productRepository.save(product1);
    }

    @Test
    void ProductTest2(){
        Product product1 = new Product();
        product1.setName("펜");
        product1.setPrice(1000);
        product1.setStock(100);
        product1.setCreatedAt(LocalDateTime.now());
        product1.setUpdatedAt(LocalDateTime.now());
        productRepository.save(product1);
    }
    // @Test
    // void QueryTest(){
    //     Optional<Product> tmp = productRepository.findByNumber(2L);

    //     if (tmp.isPresent()){
    //         Product product = tmp.get();
    //         while(true){
    //             System.out.println(product.getName());
    //         }
    //     }
    // }
    @Test
    void Mytest(){
        System.out.println(productRepository.findByNameOrderByNumberAsc("펜"));
        System.out.println("______________________");
        System.out.println(productRepository.findByNumber(2L));
    }
    @Test
    void QueryTest(){
        System.out.println(productRepository.findByName("펜"));
    }


}
