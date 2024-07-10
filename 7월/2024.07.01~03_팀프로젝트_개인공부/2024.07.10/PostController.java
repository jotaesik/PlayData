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
    
    @PostMapping(value = "/member")
    public String postMember(@RequestBody Map<String,Object> postData){
        StringBuilder sb = new StringBuilder();


        postData.entrySet().forEach(map ->{
            sb.append(map.getKey() + " : " + map.getValue() + "\n");
        });
        return sb.toString();
    }
    @PostMapping(value = "/member2")
    public String postMemberDto(@RequestBody MemberDto memberDto){
        return memberDto.toString();
    }
    // http://ip:8080/api/v1/post-api/member2
    // {
    //     "name" : "encore",
    //     "email" : "fasdf",
    //     "phone" : "010"
    // }
    






}

