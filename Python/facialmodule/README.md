# KubixSquare React-Native Face Recognition Module
## Setting up Django API Project for Face Recognition (first time only)
```
bash
cd Python
virtualenv -p python3.6 env
source ./env/bin/activate
sudo apt-get install cmake
pip install -r requirements.txt
```
## Running the Django API Project for Face Recognition
```
bash
cd Python
source ./env/bin/activate
cd facialmodule/src
python manage.py runserver 0.0.0.0:4002
```
## Creating a public server for Django API project
Download [ngrok](https://ngrok.com/) and extract files on your PC and export the path to ngrok file to the System Environment PATH variable and run
```
ngrok http 8000
```
You'll get a link to access the Django API Project outside the home network.

---

## API endpoints
### **For face training:**
> **API endpoint:** ```/face_detection/train/``` <br>
> **Method:** POST <br>
> **Parameters:**<br>
> 1. **image**<br>
> **Type:** Image<br>
> **Description:** Single image file with 1 person in image.
> 2. **url**<br>
> **Type:** URL<br>
> **Description:** Single image url with 1 person in image.
> 3. **name**<br>
> **Type:** String<br>
> **Description:** Name of the person.
> 4. **resume** (optional)<br>
> **Type:** Boolean<br>
> **Description:** Resume training or overwrite all previous trainings.<br>
> 
> **NOTE:** Use either ```image``` or ```url``` parameter to send images.

### **For face recognition:**
> **API endpoint:** ```/face_detection/detect/```<br>
> **Method:** POST <br>
> **Parameters:**<br>
> 1. **image**<br>
> **Type:** Image<br>
> **Description:** Single image file with 1 person in image.
> 2. **url**<br>
> **Type:** URL<br>
> **Description:** Single image url with 1 person in image.
> 
> **NOTE:** Use either ```image``` or ```url``` parameter to send images.
