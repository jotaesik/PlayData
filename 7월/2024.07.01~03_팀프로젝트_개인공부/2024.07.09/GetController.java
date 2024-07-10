package com.example.demo.controller;

import com.example.demo.dto.MemberDto;

import io.swagger.v3.oas.annotations.Parameter;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/vi/get-api") //주소를 이렇게 만들거야...
//ip:port/api/vi/get-api/hi
public class GetController {
    @RequestMapping(value = "/hi",method = RequestMethod.GET)
    public String GetHi(){
        return "hi";
    }
    //ip:port/api/vi/get-api/variable1/하하하하
    @GetMapping(value = "/variable1/{variable}")
    public String getVariable(@PathVariable String variable){
        return variable;
    }
    // @GetMapping(value = "/variable1/{variable}")
    // public String getVariable(@PathVariable(value = "variable") String var){
    //     return var;
    // }
   //http://ip:port/api/v1/get-api/request1?name=name&email=email&phone=010
   @GetMapping(value = "/request1")
   public String getRequestParam1(

       @Parameter (description = "이름을 넣어")
       @RequestParam String name,
       @Parameter (description = "이메일을 넣어")
       @RequestParam String email,
       @Parameter (description = "번호 넣어")
       @RequestParam String phone
   ){
       return name + " " + email + " " + phone;
   }

   @GetMapping(value = "/request3")
   public String getRequestParam3(MemberDto memberDto){
        return memberDto.toString();
   }


}
