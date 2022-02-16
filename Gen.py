<?php
    // EDIT THIS: Insert secret and site key from Google https://www.google.com/recaptcha/admin#list
    $googleRecaptchaSecret = '6L...';
    $googleSiteKey         = '6J...';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Google reCaptha Demo</title>
    <script src='https://www.google.com/recaptcha/api.js'></script>
    <style>
    <!--
        body {
            font-family: Helvetica;
            font-size: 1.2em;
        }
        td {
            padding: 8px;
        }
        h1 {
            color: white;
            padding: 9px;
            border-radius: 8px;
            background-color: #C9A;
        }
        form {
            background-color: #EDC;
            border-radius: 8px;
            padding: 9px;
        }
        .ok { color: green; }
        .ko { color: red;}
    -->
    </style>
</head>
<body>
<h1>Google <em>re</em>Captha Demo</h1>
<?php
    // Get form parameters
    $input = $_REQUEST['input1'];
    $captcha = $_REQUEST['g-recaptcha-response'];
    $response=json_decode(file_get_contents("https://www.google.com/recaptcha/api/siteverify?secret=" . $googleRecaptchaSecret . 
            "&response=".$captcha."&remoteip=".$_SERVER['REMOTE_ADDR']), true);
    if (isset($input)) {
        if ($response['success']) {
            print '<h2 class="ok">reCaptha has been validated!</h2>';
        } else {
            print '<h2 class="ko">reCaptha has not been validated!</h2>';
        }
        print "<h3>Data received  (\$_REQUEST)</h3><pre>";
        print_r($_REQUEST);
        print "\n</pre>
        <h3>Response from Google</h3><pre>\n";
        print_r($response);
        print "</pre>\n";
    }
?>

<form action="?">
<!-- Hidden Fields -->

<table>
    <tr>
        <td>Sample Input field:</td>
        <td><input name="input1"></td>
    </tr>
    <tr>
        <td colspan="2">
        <div class="g-recaptcha" data-callback="enableBtn" data-sitekey="<?php echo $googleSiteKey; ?>"></div>
        </td>
    </tr>

    <tr>
        <td></td>
        <td><input type="submit" id="buttonSubmit"></td>
    </tr>

</table>
</form>

<script>
// disable submit button until user clicks "I'm not a robot"
document.getElementById("buttonSubmit").disabled = true;
function enableBtn(){
    document.getElementById("buttonSubmit").disabled = false;
}
</script>

</body>
</html>

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
# Colorama is a module to color the python outputs
# 1. You have to install python with pip
# 2. go to your commandline and type:
#	linux: sudo pip install colorama
#	windows + mac: pip install colorama
# 3. wait for the download and then create a new python file
# 4. use the module colorama
import colorama
from colorama import Fore, Back, Style
# 5. the best way is to use colorama with f-strings
colorama.init(autoreset=True)#auto resets your settings after every output

print(f"{Fore.GREEN}green is one of the colors, there are many other colors!")Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL


websocker-client
<?php

function handshake($connect) 
{ //Функция рукопожатия
    $info = array();

    $line = fgets($connect);
    print_r($line);

    $header = explode(' ', $line);
    $info['method'] = $header[0];
    $info['uri'] = $header[1];
    print_r($info);

    //считываем заголовки из соединения
    while ($line = rtrim(fgets($connect))) 
    {
        if (preg_match('/\A(\S+): (.*)\z/', $line, $matches)) 
        {
            $info[$matches[1]] = $matches[2];
        } else {
            break;
        }
    }

    $address = explode(':', stream_socket_get_name($connect, true)); //получаем адрес клиента
    $info['ip'] = $address[0];
    $info['port'] = $address[1];

    if (empty($info['Sec-WebSocket-Key'])) 
    {
        return false;
    }
    else{
        echo "Sec-WebSocket-Key is ".$info['Sec-WebSocket-Key']."\r\n";
    }

    //отправляем заголовок согласно протоколу вебсокета
    $SecWebSocketAccept = base64_encode(pack('H*', sha1($info['Sec-WebSocket-Key'] . '258EAFA5-E914-47DA-95CA-C5AB0DC85B11')));
    $upgrade = "HTTP/1.1 101 Web Socket Protocol Handshake\r\n" .
        "Upgrade: websocket\r\n" .
        "Connection: Upgrade\r\n" .
        "Sec-WebSocket-Accept:".$SecWebSocketAccept."\r\n\r\n";
    fwrite($connect, $upgrade);

    return $info;
}

function websock_decode($data)
{
    $bytes = $data;
    $data_length = "";
    $mask = "";
    $coded_data = "" ;
    $decoded_data = "";        
    $data_length = $bytes[1] & 127;
    if ($data_length === 126)
    {
            $mask = substr($bytes, 4, 8);
            $coded_data = substr($bytes, 8);
    }
    else if ($data_length === 127)
    {
            $mask = substr($bytes, 10, 14);
            $coded_data = substr($bytes, 14);
    }
    else
    {
            $mask = substr($bytes, 2, 6);
            $coded_data = substr($bytes, 6);
    }
    for ($i = 0; $i < strlen($coded_data); $i++)
    {
            $decoded_data .= $coded_data[$i] ^ $mask[$i%4];
    }
    //echo "Server Received->".$decoded_data."\r\n";
    return $decoded_data;
}

header("Content-Type: text/plain; charset=utf-8");
error_reporting(E_ALL ^ E_WARNING);
set_time_limit(0);
ob_implicit_flush();

$NULL = NULL;
$client_socket = array();

echo "-= Server =-\n\n";     

$address = 'localhost';     
$port    = 10001;     

$operators_online = array();




$connects = array();

$socket = stream_socket_server("tcp://127.0.0.1:10001", $errno, $errstr);
if (!$socket) 
{
    echo "socket unavailable<br />";
    die($errstr. "(" .$errno. ")\n");
}

while(true)
{

    $read = $connects;
    $read []= $socket;
    $write = $except = null;

    if (!stream_select($read, $write, $except, null)) 
    {
        break;
    }

    if (in_array($socket, $read)) 
    {//есть соединение - делаем handshake
        //принимаем новое соединение и производим рукопожатие:
        if (($connect = stream_socket_accept($socket, -1))) 
        {
            if ($info = handshake($connect))
            {
                $connects[] = $connect;//добавляем его в список необходимых для обработки
                echo "Принято подключение (". count($connects) .")\r\n";
            }
        }
        unset($read[ array_search($socket, $read) ]);
    }

    //проверяем на наличие новых соединений
    foreach($connects as $key => $client)
    {
        if(in_array($client, $read))
        {
            //если соединение есть...
        $input = fread($client, 100000);

            if($input !== false)
            {
                //---вот здесь происходит зло!!!-----
        $input = trim($input);
                echo websock_decode($input);
        //----------------------------------
            }
        }
    }

    socket_close($client);
    $read = $connects;
    $read[] = $socket;
}
?>
