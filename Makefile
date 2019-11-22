prepenv:
	@echo "*** Creating Virtual Environment ***"
	( \
		python3 -m venv .venv; \
		source .venv/bin/activate; \
		pip install --upgrade pip; \
		pip install -r requirements.txt; \
)

topology:
	@echo "*** Initialize virl Lab Topology ***"
	(\
		cd init-network;\
		ansible-playbook init-dc.yaml;\
		cd ..;\
)

cleanup:
	@echo "*** Cleaning up Previous SSH Keys for Test Hosts ***"
	( \
		ssh-keygen -R 172.16.30.101;\
		ssh-keygen -R 172.16.30.102;\
		ssh-keygen -R 172.16.30.111;\
		ssh-keygen -R 172.16.30.112;\
		ssh-keygen -R 172.16.30.121;\
		ssh-keygen -R 172.16.30.122;\
)
	@echo "*** Remove Previous Demo outputs ***"
	(\
		rm -f config-gen/output/*.txt;\
		rm -rf server-access/genie/learn*/;\
		rm -rf server-access/genie change*/;\
		rm -rf server-access/genie diff_interface_nxos_n9k*;\
)
