package io.github.rushi412.socialplatformapp.repository;

import io.github.rushi412.socialplatformapp.model.Post;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PostRepository extends JpaRepository<Post, Long> {
}
