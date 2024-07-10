package com.example.demo.dto;

import io.swagger.v3.oas.annotations.media.Schema;

public class MemberDto {
    private String name;
    private String email;
    private String phone;
    public String getName(){
        return name;
    }
    @Schema (description = "이름넣어!!")
    public void setName(String name){
        this.name = name;
    }
    public String getEmail(){
        return email;
    }
    @Schema (description = "이메일넣어!!")
    public void setEmail(String email){
        this.email = email;
    }
    public String getPhone(){
        return phone;
    }
    @Schema (description = "폰넣어!!")
    public void setPhone(String phone){
        this.phone = phone; 
    }
    @Override
    public String toString(){
        return "MemberDT{" +
            "name='" + name + '\'' +
            ", email='" + email + '\'' +
            ", phone='" + phone + '\'' +
            '}';
    }

}


