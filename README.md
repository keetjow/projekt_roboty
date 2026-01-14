# Projekt zaliczeniowy – Narzędzia i oprogramowanie dla systemów robotycznych

## Autorzy
- Wojciech Gandziarowski
- Kacper Gadomski

---

![Demo](gifdemo.gif)


---

## Uruchamianie projektu na hoście

```bash
colcon build --packages-select robot_interface_control
source install/setup.bash
export TURTLEBOT3_MODEL=waffle_pi
ros2 launch robot_interface_control robot_control.launch.py
```

---

## Budowanie obrazu Docker

```bash
docker build -t robot_interface_control .
```

---

## Uruchamianie projektu w Dockerze

```bash
bash docker_run.sh
export TURTLEBOT3_MODEL=waffle_pi
ros2 launch robot_interface_control robot_control.launch.py
```

---

## Ważne informacje

W środowisku kontenerowym może wystąpić warunek wyścigu pomiędzy inicjalizacją symulatora Gazebo a procesem wstawiania modelu robota do świata symulacji. W rzadkich przypadkach skutkuje to uruchomieniem pustego świata bez załadowanego modelu TurtleBot3.

W takiej sytuacji należy przerwać działanie launch'a (`Ctrl+C`), pozostać w powłoce kontenera i ponownie uruchomić polecenie startowe. Przy kolejnym uruchomieniu, po pełnej inicjalizacji Gazebo, model robota zostanie poprawnie załadowany.

