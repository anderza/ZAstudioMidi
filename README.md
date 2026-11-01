# ZaDrumsMidi

Android-приложение, которое играет партию ударных из MIDI-файлов записанными сэмплами (FluidR3 GM, лицензия MIT).
Установки: Стандарт, Рок, Панк-рок, Модерн, Поп, Электро 808. Есть миксер с фейдерами, Overhead и Ambience, редактор дорожек и сохранение.

## Скачать APK

Готовый APK лежит в последнем релизе: **Releases → Latest → MidiDrums.apk**. Его собирает GitHub Actions при каждом push в `main`.

## Как устроено

- `web/template.html` — сам плеер (HTML, CSS, JS).
- `web/kitdata.json` — встроенные сэмплы барабанов.
- `web/build.py` собирает из них `app/src/main/assets/index.html`, единый файл, который работает без интернета.
- `app/` — Android-обёртка: WebView, выбор MIDI-файлов, сохранение MIDI в «Загрузки», кнопка «Назад» закрывает открытые панели.

Сборка локально: `python3 web/build.py && ./gradlew assembleRelease` (нужны JDK 17 и Android SDK).
