FROM golang:alpine as builder
RUN mkdir /build
ADD . /build/
WORKDIR /build

RUN go build -o main .
FROM alpine

RUN echo 'PbI6bI{изгибы которого хочется гладить, лизать, просыпаясь ночью, но ведь ты всё равно крючок}' > /flag.txt

RUN adduser -S -D -H -h /app appuser
USER appuser
COPY --from=builder /build/main /app/
WORKDIR /app


CMD ["./main"]
