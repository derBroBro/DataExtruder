# About
The idea behind this project is, that you often have some centralizes systems containing your data. From these you want to generate several kind of content. This content could be html, markdown, terraform code or a lot more. 
Exaclty this is done by the utility. It takes a data-source and transforms it into content.  
The transformation/rendering is done by [cookiecutter](https://github.com/cookiecutter/cookiecutter) which offers jinja2 templating for more complex projects. 
The data can be loaded from several source.   
  
Currently supported:
- [Directus](https://github.com/directus/directus)
  
In planning:
- Google Sheets

> Please note: [python-sdk](https://github.com/vvatelot/directus-sdk-python) is included directly, as no pip package is available during creation. Full credtis are going to the creator for this part!  
  
# Usage
Create a json file with the required information included.
Call the CLI as follow: ```app.py --template git+https://foo.bar```  
## Installation
Run `pip install DataExtruder`

## Paramters
| Paramter        | Default           | Description  |
| ------------- | ------------- | ----- |
| --config      | config.josn | The config file used |
| --template      | NONE | The template folder or url used |
| --target      | target | The output directory |
| --log-level      | INFO | The log level |

# Modules
## Directus
Example

``` 
{   
    "source_type": "directus",
    "url": "http://localhost:8080",
    "username": "email@example.com",
    "password": "yourpasswordHere",
    "model": [
        {
            "name": "users",
            "collection": "employee",
            "fields": [
                "*"
            ]
        }
}
```

Some variables can be overwritten by Environment variables.  
`username` - `DATAEXTRUDER_DIRECTUS_USERNAME`  
`password` - `DATAEXTRUDER_DIRECTUS_PASSWORD`  
