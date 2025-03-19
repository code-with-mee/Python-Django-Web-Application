<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django Command List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            background: #007bff;
            color: white;
            padding: 10px;
            border-radius: 5px;
        }
        pre {
            background: #282c34;
            color: #61dafb;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            background: #eee;
            margin: 5px 0;
            padding: 8px;
            border-radius: 4px;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <h1>Django Command List</h1>
    <div class="container">

        <h2>Basic Project Setup & Management</h2>
        <ul>
            <li><pre>django-admin startproject &lt;project_name&gt; .</pre> – Create a new Django project.</li>
            <li><pre>python manage.py startapp &lt;app_name&gt;</pre> – Create a new Django app.</li>
            <li><pre>python manage.py runserver</pre> – Start the development server.</li>
            <li><pre>python manage.py runserver &lt;port&gt;</pre> – Start the server on a specific port.</li>
        </ul>

        <h2>Database Management</h2>
        <ul>
            <li><pre>python manage.py makemigrations</pre> – Generate new migrations.</li>
            <li><pre>python manage.py migrate</pre> – Apply migrations.</li>
            <li><pre>python manage.py sqlmigrate &lt;app_name&gt; &lt;migration_number&gt;</pre> – View raw SQL.</li>
            <li><pre>python manage.py showmigrations</pre> – List all migrations.</li>
            <li><pre>python manage.py flush</pre> – Reset the database.</li>
        </ul>

        <h2>User & Authentication Management</h2>
        <ul>
            <li><pre>python manage.py createsuperuser</pre> – Create a superuser.</li>
            <li><pre>python manage.py changepassword &lt;username&gt;</pre> – Change user password.</li>
        </ul>

        <h2>Shell & Data Management</h2>
        <ul>
            <li><pre>python manage.py shell</pre> – Open interactive Django shell.</li>
            <li><pre>python manage.py dumpdata &lt;app_name.ModelName&gt;</pre> – Export data.</li>
            <li><pre>python manage.py loaddata &lt;filename&gt;</pre> – Import data.</li>
        </ul>

        <h2>Testing & Debugging</h2>
        <ul>
            <li><pre>python manage.py test</pre> – Run all tests.</li>
            <li><pre>python manage.py test &lt;app_name&gt;</pre> – Run tests for a specific app.</li>
            <li><pre>python manage.py check</pre> – Check for project issues.</li>
        </ul>

        <h2>Static Files & Media</h2>
        <ul>
            <li><pre>python manage.py collectstatic</pre> – Collect static files.</li>
            <li><pre>python manage.py findstatic &lt;file_name&gt;</pre> – Find a static file.</li>
        </ul>

        <h2>Custom Django Commands</h2>
        <ul>
            <li><pre>python manage.py &lt;custom_command&gt;</pre> – Run a custom command.</li>
        </ul>

        <h2>Additional Commands</h2>
        <ul>
            <li><pre>python manage.py diffsettings</pre> – Show project settings differences.</li>
            <li><pre>python manage.py inspectdb</pre> – Generate models from an existing database.</li>
            <li><pre>python manage.py migrate --fake</pre> – Mark migrations as applied.</li>
        </ul>

    </div>

</body>
</html>
