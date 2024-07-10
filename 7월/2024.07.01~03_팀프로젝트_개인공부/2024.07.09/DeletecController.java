package com.example.demo.controller;
import com.example.demo.dto.MemberDto;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/api/v1/delete-api")
public class DeleteController {
    @DeleteMapping(value = "/{variable}")
    public String DeleteVarible(@PathVariable String variable ){
        return variable;
    }


    // http://ip:8080/api/v1/delete-api/request1?email=value
    @DeleteMapping(value = "/request1")
    public String getRequestParam1(@RequestParam String email){
        return "e-mail : " + email;
    }
   
}
