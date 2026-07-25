package io.github.rushi412.socialplatformapp.service;

import io.github.rushi412.socialplatformapp.model.User;

public interface UserService {
    User findByUsername(String username);

    User save(User userDto);

}
