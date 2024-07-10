package com.encore.dbtest.data.dao.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import com.encore.dbtest.data.entity.Product;
import com.encore.dbtest.data.dao.ProductDAO;
import com.encore.dbtest.data.repository.ProductRepository;

import java.time.LocalDateTime;
import java.util.Optional;

@Component
public class ProductDAOImpl implements ProductDAO {
    
    private ProductRepository productRepository;

    @Autowired
    public ProductDAOImpl(ProductRepository productRepository){
        this.productRepository = productRepository;
    }

    @Override
    public Product insertProduct(Product product){
        Product savedProduct = productRepository.save(product);
        return savedProduct;
    }

    @Override
    public Product selectProduct(Long number){
        Product selectedProduct = productRepository.getReferenceById(number);
        return selectedProduct;
    }

    public void deleteProduct(Long number) throws Exception{
        Optional<Product> selectedProduct = productRepository.findById(number);

        if (selectedProduct.isPresent()){
            Product product = selectedProduct.get();
            productRepository.delete(product);
        }else{
            throw new Exception();
        }
    }

    public Product updateProductName(Long number, String name) throws Exception{
        Optional<Product> selectedProduct = productRepository.findById(number);

        Product updateProduct;
        if (selectedProduct.isPresent()){
            Product product = selectedProduct.get();

            product.setName(name);
            product.setUpdatedAt(LocalDateTime.now());

            updateProduct = productRepository.save(product);

        }else{
            throw new Exception();
        }
        return updateProduct;
    }
    
}
