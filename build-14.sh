#!/bin/bash

# Odoo 14

modules=( odoo_academy )
src_dir=.
#target_dir=/opt/odoo/custom/addons/
target_dir=/opt/custom-v14/addons/
odoo_user=odoo
odoo_service=/etc/init.d/odoo-server

# svn update

for mod_name in "${modules[@]}";
do
   # in Python: se va executa o comanda de ssystem de operare si se va verifica rezultatul executiei (adica avem cod de eroare sau nu!)
   echo sudo $mod_name $src_dir $target_dir

   echo sudo rm -rf  ${target_dir}/${mod_name}
   sudo rm -rf  ${target_dir}/${mod_name}

   echo sudo cp -r ./${mod_name} ${target_dir}
   sudo cp -r ./${mod_name} ${target_dir}

   echo sudo chown -R ${odoo_user}:${odoo_user} ${target_dir}
   sudo chown -R ${odoo_user}:${odoo_user} ${target_dir}
done
echo sudo ${odoo_service} stop
#sudo ${odoo_service} stop

echo sudo ${odoo_service} start
#sudo ${odoo_service} start
