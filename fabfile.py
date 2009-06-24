config.fab_hosts = ['alertante@beta.alertante.net']

def update():
    local("git push")
    deploy()

def deploy():
    run("cd ~/src/alertante; git pull")
    reload()
    
def reload():
    run("touch ~/src/alertante/deploy/project.wsgi")
