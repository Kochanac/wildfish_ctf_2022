package sharded_map

import (
	"fmt"
)

type UserMap struct {
	pairs []Pair
}

func NewUserMap() *UserMap {
	return &UserMap{}
}

func sortSlice(ps []Pair) {
	for i := 0; i < len(ps); i++ {
		for j := 0; j < len(ps); j++ {
			if i > j && ps[i].Key < ps[j].Key {
				ps[i], ps[j] = ps[j], ps[i]
			}
		}
	}
}

func (m *UserMap) Add(p Pair) error {
	for _, op := range m.pairs {
		if op.Key == p.Key {
			return fmt.Errorf("key already exists %s", p.Key)
		}
	}
	m.pairs = append(m.pairs, p)
	sortSlice(m.pairs)
	return nil
}

func (m *UserMap) Get(key string) int {
	l, r := 0, len(m.pairs)
	for r-l > 1 {
		c := (l + r) / 2
		if m.pairs[c].Key <= key {
			l = c
		} else {
			r = c
		}
	}
	return m.pairs[l].Value
}

type Pair struct {
	Key   string
	Value int
}
