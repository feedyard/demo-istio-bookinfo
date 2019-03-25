
from invoke import task

@task
def test(ctx):
    ctx.run('for from in "version1" "version2" "legacy"; do for to in "version1" "version2" "legacy"; do kubectl exec $(kubectl get pod -l app=sleep -n ${from} -o jsonpath={.items..metadata.name}) -c sleep -n ${from} -- curl "http://httpbin.${to}:8000/ip" -s -o /dev/null -w "sleep.${from} to httpbin.${to}: %{http_code}\n"; done; done')
