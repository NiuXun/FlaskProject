from . import assets
from flask import render_template, redirect, url_for
from app.models import Server, HostGroup, Assets, Tag, IDC, Vendor, DeviceModel
from app.home.views import login_required
from app.assets.forms import ServerForm, VendorForm,DeviceModelForm


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
    if form.validate_on_submit():
        data = form.data
    return render_template('assets/server_add.html', form=form)


# 编辑主机
@assets.route('/server_edit/<int:id>/')
@login_required
def server_edit(id=None):
    return render_template('assets/server_edit.html')


# 删除主机
@assets.route('/server_delete/<int:id>/')
def server_delete(id=None):
    return redirect(url_for('assets.host_list', page=1))


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
    return render_template('assets/host_group_add.html')


# 编辑主机组
@assets.route('/host_group_edit/<int:id>/')
def host_group_edit(id=None):
    return render_template('assets/host_group_edit.html')


# 删除主机组
@assets.route('/host_group_delete/<int:id>/')
def host_group_delete(id=None):
    return redirect(url_for('assets.host_list', page=1))


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
    return render_template('assets/idc_add.html')


# 编辑IDC
@assets.route('/idc_edit/<int:id>/')
def idc_edit(id=None):
    return render_template('assets/idc_edit.html')


# 删除IDC
@assets.route('/idc_delete/<int:id>/')
def idc_delete(id=None):
    return redirect(url_for('assets.idc_list', page=1))


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
    return render_template('assets/assets_add.html')


# 编辑资产
@assets.route('/assets_edit/<int:id>/')
def assets_edit(id=None):
    return render_template('assets/assets_edit.html')


# 删除资产
@assets.route('/assets_delete/<int:id>/')
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
    return render_template('assets/tag_add.html')


# 编辑标签
@assets.route('/tag_edit/<int:id>/')
def tag_edit(id=None):
    return render_template('assets/tag_edit.html')


# 删除标签
@assets.route('/tag_delete/<int:id>/')
def tag_delete(id=None):
    return redirect(url_for('assets.tag_list', page=1))


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
    return render_template('assets/vendor_add.html', form=form)


# 编辑厂商
@assets.route('/vendor_edit/<int:id>/')
def vendor_edit(id=None):
    return render_template('assets/vendor_edit.html')


# 删除厂商
@assets.route('/vendor_delete/<int:id>/')
def vendor_delete(id=None):
    return redirect(url_for('assets.vendor_list', page=1))


# 设备型号列表
@assets.route('/device_model_list/<int:page>/', methods=['GET'])
def device_model_list(page=None):
    if page is None:
        page = 1
    page_data = DeviceModel.query.order_by(DeviceModel.id.desc()).paginate(page=page, per_page=10)
    return render_template('assets/device_model_list.html', page_data=page_data)


# 新增设备型号
@assets.route('/device_model_add/', methods=['GET', 'POST'])
def device_model_add():
    form = DeviceModelForm()
    if form.validate_on_submit():
        data = form.data
    return render_template('assets/device_model_add.html', form=form)


# 编辑设备型号
@assets.route('/device_model_edit/<int:id>/')
def device_model_edit(id=None):
    return render_template('assets/device_model_edit.html')


# 删除设备型号
@assets.route('/device_model_delete/<int:id>/')
def device_model_delete(id=None):
    return redirect(url_for('assets.device_model_list', page=1))