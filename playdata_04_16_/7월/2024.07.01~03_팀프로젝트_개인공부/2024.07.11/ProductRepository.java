package com.springboot.advanced_jpa.data.repository;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import com.springboot.advanced_jpa.data.entity.Product;

public interface ProductRepository extends JpaRepository<Product,Long>{
    //쿼리 예제
    Optional<Product> findByNumber(long number);
    // List<Product> findAllbyName(String name);
    // Product queryByNumber(Long number);

    // exists..By (예제 8.2)
    boolean existsByNumber(Long number);

    // count..By (예제 8.3)
    long countByName(String name);

    // delete..By, remove..By (예제 8.4)
    void deleteByNumber(Long number);
    long removeByName(String name);

    // …First<number>…, …Top<number>… (예제 8.5)
    List<Product> findFirst5ByName(String name);
    List<Product> findTop10ByName(String name);

    /* 쿼리 메소드의 조건자 키워드 */

    // Is, Equals (생략 가능) (예제 8.6)
    // Logical Keyword : IS , Keyword Expressions : Is, Equals, (or no keyword)
    // findByNumber 메소드와 동일하게 동작
    Product findByNumberIs(Long number);
    Product findByNumberEquals(Long number);

    // (Is)Not (예제 8.7)
    Product findByNumberIsNot(Long number);
    Product findByNumberNot(Long number);

    // (Is)Null, (Is)NotNull (예제 8.8)
    List<Product> findByUpdatedAtNull();
    List<Product> findByUpdatedAtIsNull();
    List<Product> findByUpdatedAtNotNull();
    List<Product> findByUpdatedAtIsNotNull();

    // And, Or (예제 8.10)
    Product findByNumberAndName(Long number, String name);
    Product findByNumberOrName(Long number, String name);

    // (Is)GreaterThan, (Is)LessThan, (Is)Between (예제 8.11)
    List<Product> findByPriceIsGreaterThan(Long price);
    List<Product> findByPriceGreaterThan(Long price);
    List<Product> findByPriceGreaterThanEqual(Long price);
    List<Product> findByPriceIsLessThan(Long price);
    List<Product> findByPriceLessThan(Long price);
    List<Product> findByPriceLessThanEqual(Long price);
    List<Product> findByPriceIsBetween(Long lowPrice, Long highPrice);
    List<Product> findByPriceBetween(Long lowPrice, Long highPrice);

    // (Is)Like, (Is)Containing, (Is)StartingWith, (Is)EndingWith (예제 8.12)
    List<Product> findByNameLike(String name);
    List<Product> findByNameIsLike(String name);

    List<Product> findByNameContains(String name);
    List<Product> findByNameContaining(String name);
    List<Product> findByNameIsContaining(String name);

    List<Product> findByNameStartsWith(String name);
    List<Product> findByNameStartingWith(String name); 
    List<Product> findByNameIsStartingWith(String name);

    List<Product> findByNameEndsWith(String name);
    List<Product> findByNameEndingWith(String name);
    List<Product> findByNameIsEndingWith(String name);

    /* 정렬 처리하기 */

    // Asc : 오름차순, Desc : 내림차순 (예제 8.13)
    List<Product> findByNameOrderByNumberAsc(String name);
    List<Product> findByNameOrderByNumberDesc(String name);

    // 여러 정렬 기준 사용하기, And를 붙이지 않음 (예제 8.14)
    List<Product> findByNameOrderByPriceAscStockDesc(String name);


    @Query("SELECT p FROM Product p WHERE p.name = ?1")
    List<Product> findByName(String name);
}   
