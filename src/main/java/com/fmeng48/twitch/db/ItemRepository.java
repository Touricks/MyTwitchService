package com.fmeng48.twitch.db;
import com.fmeng48.twitch.db.entity.ItemEntity;
import org.springframework.data.repository.ListCrudRepository;
public interface ItemRepository extends ListCrudRepository<ItemEntity, Long> {
    // SQL: SELECT * FROM items WHERE twitchId = <twitchId>;
    ItemEntity findByTwitchId(String twitchId);
    ItemEntity findAllById(Long id);
}