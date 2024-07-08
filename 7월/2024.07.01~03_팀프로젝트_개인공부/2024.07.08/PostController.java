package com.example.demo.controller;
import com.example.demo.dto.MemberDto;
import java.util.Map;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMethod;


@RestController
@RequestMapping("/api/v1/post-api")
public class PostController {


    @RequestMapping(value = "/domain", method = RequestMethod.POST)
    // @PostMapping("/domain")
    public String postExam(){
        return "post api test";
    }
   
}

