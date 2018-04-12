from . import assets
from flask import render_template, redirect, url_for, flash, request
from app.models import Server, HostGroup, Assets, Tag, IDC, Vendor
from app.home.views import login_required
from app.assets.forms import ServerForm, VendorForm, HostGroupForm, IDCForm, TagForm, AssetsForm
from app import db
from datetime import datetime


# 主机列表
@assets.route('/server_list/<int:page>/', methods=['GET'])
@login_required
def server_list(page=None):
    if page is None:
        page = 1
    page_data = Server.query.order_by(Server.id.desc()).paginate(page=page, per_page=10)
    return render_template('assets/server_list.html', page_data=page_data)


# 新增主机
@assets.route('/server_add/', methods=['GET', 'POST'])
@login_required
def server_add():
    form = ServerForm()
    form.groups.choices = [(v.id, v.name) for v in HostGroup.query.all()]
    form.vendor.choices = [(v.id, v) for v in Vendor.query.all()]
    if form.validate_on_submit():
        data = form.data
        server_count = Server.query.filter_by(name=data['name']).count()
        if server_count == 1:
            flash(message='该服务器已存在', category='error')
            return redirect(url_for('assets.server_add'))
        try:
            server = Server(
                sn_number=data['sn_number'],
                name=data['name'],
                system_version=data['system_version'],
                ip_address=data['ip_address'],
                mac_address=data['mac_address'],
                RAID_type=','.join(map(lambda v: str(v), data['RAID_type'])),
                cpu_type=data['cpu_type'],
                cpu_count=data['cpu_count'],
                memory_capacity=data['memory_capacity'],
                disk_capacity=data['disk_capacity'],
                disk_type=data['disk_type'],
                network_card_type=data['network_card_type'],
                network_card_count=data['network_card_count'],
                power_count=data['power_count'],
                vendor_id=int(data['vendor']),
                last_modify_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                remark=data['remark'],
            )
            db.session.add(server)
            db.session.commit()
            server = Server.query.filter_by(sn_number=data['sn_number']).first_or_404()
            for group_id in data['groups']:
                choise_group = HostGroup.query.filter_by(id=group_id).first_or_404()
                server.groups.append(choise_group)
            db.session.add(server)
            db.session.commit()
            flash(message='添加服务器成功', category='ok')
            return redirect(url_for('assets.server_add'))
        except Exception as e:
            print(e)
    return render_template('assets/server_add.html', form=form)


# 编辑主机
@assets.route('/server_edit/<int:id>/', methods=['GET', 'POST'])
@login_required
def server_edit(id=None):
    form = ServerForm()
    form.groups.choices = [(v.id, v.name) for v in HostGroup.query.all()]
    form.vendor.choices = [(v.id, v) for v in Vendor.query.all()]
    server = Server.query.get_or_404(id)
    if request.method == 'GET':
        form.vendor.data = server.vendor_id
        form.disk_type.data = server.disk_type
        form.groups.data = [(v.id) for v in server.groups]
        form.RAID_type.data = server.RAID_type
    if form.validate_on_submit():
        data = form.data
        server_count = Vendor.query.filter_by(name=data['name']).count()
        if server.name != data['name'] and server_count == 1:
            flash(message='该服务器已存在，请重新输入', category='error')
            return redirect(url_for('assets.server_edit', id=id))
        try:
            server.name = data['name']
            server.system_version = data['system_version'],
            server.ip_address = data['ip_address'],
            server.mac_address = data['mac_address'],
            server.RAID_type = ','.join(map(lambda v: str(v), data['RAID_type'])),
            server.cpu_type = data['cpu_type'],
            server.cpu_count = data['cpu_count'],
            server.memory_capacity = data['memory_capacity'],
            server.disk_capacity = data['disk_capacity'],
            server.disk_type = data['disk_type'],
            server.network_card_type = data['network_card_type'],
            server.network_card_count = data['network_card_count'],
            server.power_count = data['power_count'],
            server.vendor_id = int(data['vendor']),
            server.last_modify_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            server.remark = data['remark'],
            db.session.add(server)
            db.session.commit()

            # for group_id in data['groups']:
            #     choise_group = HostGroup.query.filter_by(id=group_id).first_or_404()
            #     server.groups.append(choise_group)
            # db.session.add(server)
            # db.session.commit()
            flash(message='修改服务器信息成功', category='ok')
            return redirect(url_for('assets.server_edit', id=id))
        except Exception as e:
            print(e)
    return render_template('assets/server_edit.html', form=form, server=server)


# 删除主机
@assets.route('/server_delete/<int:id>/', methods=['GET'])
def server_delete(id=None):
    server = Server.query.filter_by(id=id).first_or_404()
    try:
        db.session.delete(server)
        db.session.commit()
        flash(message='删除服务器成功', category='ok')
        return redirect(url_for('assets.server_list', page=1))
    except Exception as e:
        print(e)


# 主机组列表
@assets.route('/host_group_list/<int:page>/', methods=['GET'])
def host_group_list(page=None):
    if page is None:
        page = 1
    page_data = HostGroup.query.order_by(HostGroup.id.desc()).paginate(page=page, per_page=10)
    return render_template('assets/host_group_list.html', page_data=page_data)


# 新增主机组
@assets.route('/host_group_add/', methods=['GET', 'POST'])
def host_group_add():
    form = HostGroupForm()
    if form.validate_on_submit():
        data = form.data
        host_group_count = HostGroup.query.filter_by(name=data['name']).count()
        if host_group_count == 1:
            flash(message='该主机组已存在', category='error')
            return redirect(url_for('assets.host_group_add'))
        try:
            host_group = HostGroup(
                name=data['name'],
                last_modify_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                remark=data['remark'],
            )
            db.session.add(host_group)
            db.session.commit()
            flash(message='添加主机组成功', category='ok')
            return redirect(url_for('assets.host_group_add'))
        except Exception as e:
            print(e)
    return render_template('assets/host_group_add.html', form=form)


# 编辑主机组
@assets.route('/host_group_edit/<int:id>/', methods=['GET', 'POST'])
def host_group_edit(id=None):
    form = HostGroupForm()
    host_group = HostGroup.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        host_group_count = HostGroup.query.filter_by(name=data['name']).count()
        if host_group.name != data['name'] and host_group_count == 1:
            flash(message='该主机组已存在，请重新输入', category='error')
            return redirect(url_for('assets.host_group_edit', id=id))
        try:
            host_group.name = data['name']
            host_group.last_modify_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            host_group.remark = data['remark']
            db.session.add(host_group)
            db.session.commit()
            flash(message='修改主机组成功', category='ok')
            return redirect(url_for('assets.host_group_edit', id=id))
        except Exception as e:
            print(e)
    return render_template('assets/host_group_edit.html', form=form, host_group=host_group)


# 删除主机组
@assets.route('/host_group_delete/<int:id>/', methods=['GET'])
def host_group_delete(id=None):
    host_group = HostGroup.query.filter_by(id=id).first_or_404()
    try:
        db.session.delete(host_group)
        db.session.commit()
        flash(message='删除主机组成功', category='ok')
        return redirect(url_for('assets.host_group_list', page=1))
    except Exception as e:
        print(e)


# IDC列表
@assets.route('/idc_list/<int:page>/', methods=['GET'])
def idc_list(page=None):
    if page is None:
        page = 1
    page_data = IDC.query.order_by(IDC.id.desc()).paginate(page=page, per_page=10)
    return render_template('assets/idc_list.html', page_data=page_data)


# 新增IDC
@assets.route('/idc_add/', methods=['GET', 'POST'])
def idc_add():
    form = IDCForm()
    if form.validate_on_submit():
        data = form.data
        idc_count = IDC.query.filter_by(name=data['name']).count()
        if idc_count == 1:
            flash(message='该机房已存在', category='error')
            return redirect(url_for('assets.idc_add'))
        try:
            idc = IDC(
                name=data['name'],
                address=data['address'],
                last_modify_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                remark=data['remark'],
            )
            db.session.add(idc)
            db.session.commit()
            flash(message='添加机房成功', category='ok')
            return redirect(url_for('assets.idc_add'))
        except Exception as e:
            print(e)
    return render_template('assets/idc_add.html', form=form)


# 编辑IDC
@assets.route('/idc_edit/<int:id>/', methods=['GET', 'POST'])
def idc_edit(id=None):
    form = IDCForm()
    idc = IDC.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        idc_count = IDC.query.filter_by(name=data['name']).count()
        if idc.name != data['name'] and idc_count == 1:
            flash(message='该机房已存在，请重新输入', category='error')
            return redirect(url_for('assets.idc_edit', id=id))
        try:
            idc.name = data['name']
            idc.address = data['address']
            idc.last_modify_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            idc.remark = data['remark']
            db.session.add(idc)
            db.session.commit()
            flash(message='修改机房信息成功', category='ok')
            return redirect(url_for('assets.idc_edit', id=id))
        except Exception as e:
            print(e)
    return render_template('assets/idc_edit.html', form=form, idc=idc)


# 删除IDC
@assets.route('/idc_delete/<int:id>/', methods=['GET'])
def idc_delete(id=None):
    idc = IDC.query.filter_by(id=id).first_or_404()
    try:
        db.session.delete(idc)
        db.session.commit()
        flash(message='删除机房成功', category='ok')
        return redirect(url_for('assets.idc_list', page=1))
    except Exception as e:
        print(e)


# 资产列表
@assets.route('/assets_list/<int:page>/', methods=['GET'])
def assets_list(page=None):
    if page is None:
        page = 1
    page_data = Assets.query.order_by(Assets.id.desc()).paginate(page=page, per_page=10)
    return render_template('assets/assets_list.html', page_data=page_data)


# 新增资产
@assets.route('/assets_add/', methods=['GET', 'POST'])
def assets_add():
    form = AssetsForm()
    form.device_name.choices = [(v.id, v.name) for v in Server.query.all()]
    if form.validate_on_submit():
        data = form.data
    return render_template('assets/assets_add.html', form=form)


# 编辑资产
@assets.route('/assets_edit/<int:id>/', methods=['GET', 'POST'])
def assets_edit(id=None):
    return render_template('assets/assets_edit.html')


# 删除资产
@assets.route('/assets_delete/<int:id>/', methods=['GET'])
def assets_delete(id=None):
    return redirect(url_for('assets.assets_list', page=1))


# 标签列表
@assets.route('/tag_list/<int:page>/', methods=['GET'])
def tag_list(page=None):
    if page is None:
        page = 1
    page_data = Tag.query.order_by(Tag.id.desc()).paginate(page=page, per_page=10)
    return render_template('assets/tag_list.html', page_data=page_data)


# 新增标签
@assets.route('/tag_add/', methods=['GET', 'POST'])
def tag_add():
    form = TagForm()
    if form.validate_on_submit():
        data = form.data
        tag_count = Tag.query.filter_by(name=data['name']).count()
        if tag_count == 1:
            flash(message='该标签已存在', category='error')
            return redirect(url_for('assets.tag_add'))
        try:
            tag = Tag(
                name=data['name'],
                last_modify_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                remark=data['remark'],
            )
            db.session.add(tag)
            db.session.commit()
            flash(message='添加标签成功', category='ok')
            return redirect(url_for('assets.tag_add'))
        except Exception as e:
            print(e)
    return render_template('assets/tag_add.html', form=form)


# 编辑标签
@assets.route('/tag_edit/<int:id>/', methods=['GET', 'POST'])
def tag_edit(id=None):
    form = TagForm()
    tag = Tag.query.get_or_404(id)
    if form.validate_on_submit():
        data = form.data
        tag_count = Tag.query.filter_by(name=data['name']).count()
        if tag.name != data['name'] and tag_count == 1:
            flash(message='该标签已存在，请重新输入', category='error')
            return redirect(url_for('assets.tag_edit', id=id))
        try:
            tag.name = data['name']
            tag.last_modify_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            tag.remark = data['remark']
            db.session.add(tag)
            db.session.commit()
            flash(message='修改标签成功', category='ok')
            return redirect(url_for('assets.tag_edit', id=id))
        except Exception as e:
            print(e)
    return render_template('assets/tag_edit.html', form=form, tag=tag)


# 删除标签
@assets.route('/tag_delete/<int:id>/', methods=['GET'])
def tag_delete(id=None):
    tag = Tag.query.filter_by(id=id).first_or_404()
    try:
        db.session.delete(tag)
        db.session.commit()
        flash(message='删除标签成功', category='ok')
        return redirect(url_for('assets.tag_list', page=1))
    except Exception as e:
        print(e)


# 厂商列表
@assets.route('/vendor_list/<int:page>/', methods=['GET'])
def vendor_list(page=None):
    if page is None:
        page = 1
    page_data = Vendor.query.order_by(Vendor.id.desc()).paginate(page=page, per_page=10)
    return render_template('assets/vendor_list.html', page_data=page_data)


# 新增厂商
@assets.route('/vendor_add/', methods=['GET', 'POST'])
def vendor_add():
    form = VendorForm()
    if form.validate_on_submit():
        data = form.data
        vendor = Vendor.query.filter_by(name=data['name'], device_model=data['device_model']).first()
        vendor_count = Vendor.query.filter_by(name=data['name'], device_model=data['device_model']).count()
        print(vendor_count)
        print(data['name'], data['device_type'], data['device_model'])
        if vendor_count == 1 and vendor.device_model == data['device_model']:
            flash(message='该厂商已存在', category='error')
            return redirect(url_for('assets.vendor_add'))
        try:
            vendor = Vendor(
                name=data['name'],
                device_type=data['device_type'],
                device_model=data['device_model'],
                last_modify_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                remark=data['remark'],
            )
            db.session.add(vendor)
            db.session.commit()
            flash(message='添加厂商成功', category='ok')
            return redirect(url_for('assets.vendor_add'))
        except Exception as e:
            print(e)
    return render_template('assets/vendor_add.html', form=form)


# 编辑厂商
@assets.route('/vendor_edit/<int:id>/', methods=['GET', 'POST'])
def vendor_edit(id=None):
    form = VendorForm()
    vendor = Vendor.query.get_or_404(id)
    if request.method == 'GET':
        form.device_type.data = vendor.device_type
    if form.validate_on_submit():
        data = form.data
        vendor_count = Vendor.query.filter_by(name=data['name'], device_model=data['device_model']).count()
        if (vendor.name != data['name'] and vendor_count == 1) or (
                vendor.device_model != data['device_model'] and vendor_count == 1):
            flash(message='该厂商已存在，请重新输入', category='error')
            return redirect(url_for('assets.vendor_edit', id=id))
        try:
            vendor.name = data['name']
            vendor.device_type = data['device_type']
            vendor.device_model = data['device_model']
            vendor.last_modify_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            vendor.remark = data['remark']
            db.session.add(vendor)
            db.session.commit()
            flash(message='修改厂商成功', category='ok')
            return redirect(url_for('assets.vendor_edit', id=id))
        except Exception as e:
            print(e)
    return render_template('assets/vendor_edit.html', form=form, vendor=vendor)


# 删除厂商
@assets.route('/vendor_delete/<int:id>/', methods=['GET'])
def vendor_delete(id=None):
    vendor = Vendor.query.filter_by(id=id).first_or_404()
    try:
        db.session.delete(vendor)
        db.session.commit()
        flash(message='删除厂商成功', category='ok')
        return redirect(url_for('assets.vendor_list', page=1))
    except Exception as e:
        print(e)
