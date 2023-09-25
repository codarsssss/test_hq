# test_hq

http://localhost:8000/api/docs/

# цели:

## Построение системы для обучения
### Суть задания заключается в проверке знаний построения связей в БД и умение правильно строить запросы без ошибок N+1.

Перед тем, как приступить к выполнению задания, советуем изучить материалы, которые помогут в выполнении заданий:
https://docs.djangoproject.com/en/4.2/intro/tutorial01/
https://docs.djangoproject.com/en/4.2/topics/db/models/
https://docs.djangoproject.com/en/4.2/topics/db/queries/
https://docs.djangoproject.com/en/4.2/ref/models/querysets/
https://www.django-rest-framework.org/tutorial/quickstart/
https://www.django-rest-framework.org/api-guide/viewsets/
https://www.django-rest-framework.org/api-guide/serializers/


##### Построение архитектуры(3 балла)
В этом задании у нас есть три бизнес-задачи на хранение:
Создать сущность продукта. У продукта должен быть владелец. Необходимо добавить сущность для сохранения доступов к продукту для пользователя.
Создать сущность урока. Урок может находиться в нескольких продуктах одновременно. В уроке должна быть базовая информация: название, ссылка на видео, длительность просмотра (в секундах).
Урок могут просматривать множество пользователей. Необходимо для каждого фиксировать время просмотра и фиксировать статус “Просмотрено”/”Не просмотрено”. Статус “Просмотрено” проставляется, если пользователь просмотрел 80% ролика.

##### Написание запросов(7 баллов)
В этом пункте потребуется использовать выполненную вами в прошлом задании архитектуру:
Реализовать API для выведения списка всех уроков по всем продуктам к которым пользователь имеет доступ, с выведением информации о статусе и времени просмотра.
Реализовать API с выведением списка уроков по конкретному продукту к которому пользователь имеет доступ, с выведением информации о статусе и времени просмотра, а также датой последнего просмотра ролика.
Реализовать API для отображения статистики по продуктам. Необходимо отобразить список всех продуктов на платформе, к каждому продукту приложить информацию:
Количество просмотренных уроков от всех учеников.
Сколько в сумме все ученики потратили времени на просмотр роликов.
Количество учеников занимающихся на продукте.
Процент приобретения продукта (рассчитывается исходя из количества полученных доступов к продукту деленное на общее количество пользователей на платформе).


Результат выполнения:
Выполненная архитектура на базе данных SQLite с использованием Django.
Реализованные API на базе готовой архитектуры.
