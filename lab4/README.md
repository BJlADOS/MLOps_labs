# Практика по MLops команда №14 lab№4

Настроенные функциональности
Инициализация DVC: успешно настроен DVC в проекте, созданы необходимые конфигурационные файлы.

Удаленное хранилище: настроено хранилище на Google disk для хранения версий данных.

Версионирование данных:

Созданы 3 версии датасета:

Исходные данные (Pclass, Sex, Age)

Данные с заполненными пропусками в Age

Данные с one-hot encoding для Sex

Работа с Git: все изменения метаданных DVC зафиксированы в Git.

Переключение версий: успешно протестирована возможность переключения между разными версиями данных.

[Ссылка на Google disk](https://drive.google.com/drive/folders/1HE-SC2mAyXJs5uaP5f3pYc6iotEPOraR)

### Коммиты

dataset v1

```
git checkout 10c121612414872f1cf15aed80e558f47e88601c
dvc checkout
```

dataset v2

```
git checkout 77c9c978aefe1dfcb1fb23a26b75e2d8721c0b7b
dvc checkout
```

dataset v3

```
git checkout 77c9c978aefe1dfcb1fb23a26b75e2d8721c0b7b
dvc checkout
```

### .dvc

[Ссылка на .dvc](https://drive.google.com/file/d/1jENHIlY5yt9S0q_wc6JU4moPYxf5A3fy/view)