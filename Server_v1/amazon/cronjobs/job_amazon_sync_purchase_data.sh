#!/usr/bin/env bash
function run()
{
sshpass -p'newaim#2019' ssh root@192.168.1.218 > /dev/null 2>&1 << eeooff
cd /data/data-integration
/data/data-integration/kitchen.sh -rep=kettle_file_test -param:"file.repository.path=/data/scripts_repositories/data_center_testing" -job=/amazon/data/job/job_amazon_sync_purchase_data -log=/data/logs/jobs/$(date +%Y_%m_%d_%H)job_amazon_sync_purchase_data.log
exit
eeooff
echo done!
}


run

