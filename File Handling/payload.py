---
- name: Test Playbook
  hosts: all
  gather_facts: false

  tasks:

    - name: Show Target IP
      debug:
        msg: "Running on {{ target_ip }}"
