package com.encore.dbtest.data.repository;

import com.encore.dbtest.data.entity.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, Long> {

    
} 