package main

import (
	"fmt"
	"time"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"net/http"
)

func main() {
	r := chi.NewRouter()
	r.Use(middleware.RequestID)
	r.Use(middleware.Logger)
	r.Use(middleware.Recoverer)

	app := NewDivingService()

	r.Post("/register", func(w http.ResponseWriter, r *http.Request) {
		err := r.ParseForm()
		if err != nil {
			fmt.Printf("%s", err)
			return
		}

		ret := app.Register(r.Form.Get("username"), r.Form.Get("password"), 0)
		_, err = w.Write([]byte(ret))
		if err != nil {
			fmt.Printf("%s", err)
			return
		}
	})

	r.Post("/send", func(w http.ResponseWriter, r *http.Request) {
		_, err := w.Write([]byte("not implemented"))
		if err != nil {
			fmt.Printf("%s", err)
			return
		}
	})

	r.Get("/balances", func(w http.ResponseWriter, r *http.Request) {
		ret := app.Balances()
		_, err := w.Write([]byte(ret))
		if err != nil {
			fmt.Printf("%s", err)
			return
		}
	})

	r.Post("/dive", func(w http.ResponseWriter, r *http.Request) {
		err := r.ParseForm()
		if err != nil {
			fmt.Printf("%s", err)
			return
		}
		fmt.Printf("%v", r.Form)

		ret := app.Dive(r.Form.Get("username"), r.Form.Get("password"))
		_, err = w.Write([]byte(ret))
		if err != nil {
			fmt.Printf("%s", err)
			return
		}
	})

	go func() {
		for {
			select {
			case <-time.After(time.Millisecond * 5):
				app.Register(RandomString(10), RandomString(10), 1000)
			}
		}
	}()

	go func() {
		for {
			select {
			case <-time.After(time.Minute):
				panic("time to stop")
			}
		}
	}()

	err := http.ListenAndServe(":3333", r)
	if err != nil {
		fmt.Printf("failed to serve: %s", err)
	}
}
