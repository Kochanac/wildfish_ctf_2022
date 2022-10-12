package users

import (
	"fmt"
	"sync"
)

type UsersRepo struct {
	usersMap    map[string]string
	usersMapMtx *sync.Mutex
}

func NewUsersRepo() *UsersRepo {
	return &UsersRepo{
		usersMap:    make(map[string]string),
		usersMapMtx: &sync.Mutex{},
	}
}

func (r *UsersRepo) Register(user string, password string) error {
	_, ok := r.usersMap[user]
	if ok {
		return fmt.Errorf("user already exists")
	}
	r.usersMap[user] = password
	return nil
}

func (r *UsersRepo) CheckPassword(user string, password string) (bool, error) {
	pass, ok := r.usersMap[user]

	if !ok {
		return false, fmt.Errorf("user does not exist")
	}

	if pass != password {
		return false, fmt.Errorf("wrong password")
	}

	return true, nil
}

func (r *UsersRepo) ListUsers() []string {
	var res []string
	for user, _ := range r.usersMap {
		res = append(res, user)
	}
	return res
}
