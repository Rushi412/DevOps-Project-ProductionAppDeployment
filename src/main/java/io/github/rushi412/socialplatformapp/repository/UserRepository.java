package io.github.rushi412.socialplatformapp.repository;

import io.github.rushi412.socialplatformapp.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
    User findByUsername(String username);

    User save(User userDto);
}
