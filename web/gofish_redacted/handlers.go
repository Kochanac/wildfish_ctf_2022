package main

import (
	"fmt"
	sharded_map "gofish/map"
	users2 "gofish/users"
	"os"
	"strconv"
	"strings"
)

type DivingService struct {
	m     *sharded_map.ShardedUserMap
	users *users2.UsersRepo
}

func NewDivingService() *DivingService {
	return &DivingService{
		sharded_map.NewShardedUserMap(4),
		users2.NewUsersRepo(),
	}
}

func (r *DivingService) Register(user, password string, balance int) string {
	err := r.users.Register(user, password)
	if err != nil {
		return err.Error()
	}
	err = r.m.Add(sharded_map.Pair{Key: user, Value: balance})
	if err != nil {
		return err.Error()
	}
	return "ok"
}

func (r *DivingService) Dive(user, password string) string {
	_, err := r.users.CheckPassword(user, password)
	if err != nil {
		return err.Error()
	}
	balance := r.m.Get(user)

	if balance > 500 {
		f, err := os.Open("/flag.txt")
		if err != nil {
			return "task is broken, contact @kochanac"
		}
		flag := make([]byte, 1000)
		_, err = f.Read(flag)
		fmt.Println("flag", string(flag))
		if err != nil {
			return "task is broken, contact @kochanac"
		}
		return string(flag)
	}
	return "not enough money"
}

func (r *DivingService) Balances() string {
	lu := r.users.ListUsers()

	res := strings.Builder{}

	for _, user := range lu {
		res.WriteString(user)
		res.WriteString(" ")
		bal := r.m.Get(user)

		res.WriteString(strconv.Itoa(bal))
		res.WriteString("\n\n")
	}

	return res.String()
}
