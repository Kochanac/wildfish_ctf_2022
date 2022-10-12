package sharded_map

import (
	"sync"
)

type ShardedUserMap struct {
	Shards  []*UserMap
	Mutexes []*sync.Mutex
}

func NewShardedUserMap(shardCount int) *ShardedUserMap {
	var shards []*UserMap
	for i := 0; i < shardCount; i++ {
		shards = append(shards, NewUserMap())
	}

	var res ShardedUserMap
	for _, shard := range shards {
		res.Shards = append(res.Shards, shard)
		res.Mutexes = append(res.Mutexes, &sync.Mutex{})
	}

	return &res
}

func (m *ShardedUserMap) getShard(key string) int {
	hash := 0

	k := 1
	for _, x := range key {
		hash += int(x) * k
		k *= 2
	}
	return hash % len(m.Shards)
}

func (m *ShardedUserMap) Get(key string) int {
	shard := m.getShard(key)
	m.Mutexes[shard].Lock()
	defer m.Mutexes[shard].Unlock()
	return m.Shards[shard].Get(key)
}

func (m *ShardedUserMap) Add(p Pair) error {
	shard := m.getShard(p.Key)
	m.Mutexes[shard].Lock()
	defer m.Mutexes[shard].Unlock()
	return m.Shards[shard].Add(p)
}

//func (m *ShardedUserMap) Inc(key string, val int) {
//	shard := m.getShard(key)
//	m.Mutexes[shard].Lock()
//	defer m.Mutexes[shard].Unlock()
//	m.Shards[shard].Inc(key, val)
//}
