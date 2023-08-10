# Homework #6. Docker. Packing a simple script.


---
![Main workflow](https://github.com/hillel-i-python-pro-i-2023-06-23/homework__dmytro_palamarchuk__N15/actions/workflows/main-workflow.yml/badge.svg)

## 🏠 Homework

Homework related actions.

### ▶️ Run

Make all actions needed for run homework from zero. Including configuration.

```shell
make d-homework-i-run
```

### 🚮 Purge

Make all actions needed for run homework from zero.

```shell
make d-homework-i-purge
```

---

## 🛠️ Dev

### Initialize dev

Install dependencies and register pre-commit.

```shell
make init-dev
```

### ⚙️ Configure

Configure homework.

```shell
make init-configs
```

---

## 🐳 Docker

Use services in dockers.

### ▶️ Run

Just run

```shell
make d-run
```

### ⏹️Stop

Stop services

```shell
make d-stop
```

### 🚮 Purge

Purge all data related with services

```shell
make d-purge
```

---

### ▶️ Run homework.
```shell
make homework-i-run
```

### 🚮 Purge
```shell
make homework-i-purge
```

---

###  🛠️ Run tools for files from commit.
```shell
make pre-commit-run
```

###  🛠️ Run tools for all files.
```shell
make pre-commit-run-all
```
