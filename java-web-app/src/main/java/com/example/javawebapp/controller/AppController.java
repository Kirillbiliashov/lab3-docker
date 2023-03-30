package com.example.javawebapp.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AppController {

  @GetMapping("/hello")
  public String hello() {
    return "hello from docker lab 3!";
  }

}
