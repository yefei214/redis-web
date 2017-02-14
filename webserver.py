#! /usr/bin/python  
# encoding:utf-8  
  
import web
import model
import os
#root = os.path.dirname(__file__)
#render = web.template.render(os.path.join(root, '..', 'templates/'))
render = web.template.render('templates/')
# url映射
urls = (  
    '/redis/(.*)', 'Index',
)

app=web.application(urls,globals())  

# 指定模板目录，并设定公共模板  
#render=web.template.render(os.path.join(root, '..', 'templates/'),globals=t_globals)
# 首页类  
class Index:  
    form=web.form.Form(
        web.form.Dropdown('env', ['Stable', 'Test'],description='环境'),
        web.form.Dropdown('mode', ['user', 'order', 'pay'],description='模块'),
        web.form.Textarea('out',
                          #web.form.notnull,
                          rows=5,
                          cols=70,
                          description='输出'),
    )

    def GET(self, id):
        #form=self.form()
        #form.out.set_value('dddd')
        i = web.input()
        cmd = i.get('cmd', None)
        return render.index(i)

    def POST(self, id):
        i = web.input()
        if id == 'cmd':
            i.out = model.executeCommand(i.cmd, 'Stable_User')
            return render.index(i,i.cmd)
        elif id == 'set':
            model.stringSet(i.key, i.value, 'Stable_User')
            return render.index(i, 'error')
        elif id == 'get':
            i.value = model.stringGet(i.key, 'Stable_User')
            return render.index(i, 'error')
        elif id == 'del':
            i.value = model.stringDel(i.key, 'Stable_User')
            return render.index(i, 'error')
        elif id == 'hget':
            i.hvalue = model.hashGet(i.hname, i.hkey, 'Stable_User')
            return render.index(i, 'error')
        elif id == 'hdel':
            i.hvalue = model.hashDel(i.hname, i.hkey, 'Stable_User')
            return render.index(i, 'error')
        else:
            return render.index(i, 'error')
        #model.new_post(form.d.cmd,form.d.out)
        #raise web.seeother('/redis')
    def HASH(self):
        #form=self.form()
        #form.out.set_value('dddd')
        i = web.input()
        cmd = i.get('cmd', None)
        i.set('out','ggf')
        out = cmd
        return render.index(i)

# 定义404  
def notfound():  
    return web.notfound("sorry,the page you were looking for was not found")  
app.notfound=notfound  
  
# 运行  
if __name__ == '__main__':  
    app.run()