# <font color="orange">用户注册前端逻辑   </font>

register.html 文件: 

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <title>美多商城-注册</title>
    <link rel="stylesheet" type="text/css" href="css/reset.css">
    <link rel="stylesheet" type="text/css" href="css/main.css">
    <script type="text/javascript" src="js/host.js"></script>
    <script type="text/javascript" src="js/vue-2.5.16.js"></script>
    <script type="text/javascript" src="js/axios-0.18.0.min.js"></script>
</head>
<body>
    <div class="register_con">
        <div class="l_con fl">
            <a class="reg_logo"><img src="images/logo.png"></a>
            <div class="reg_slogan">商品美 · 种类多 · 欢迎光临</div>
            <div class="reg_banner"></div>
        </div>

        <div class="r_con fr">
            <div class="reg_title clearfix">
                <h1>用户注册</h1>
                <a href="/login.html">登录</a>
            </div>
            <div class="reg_form clearfix" id="app" v-cloak>
                 <form method="post" @submit.prevent="on_submit">
                    <ul>
                        <li>
                            <label>用户名:</label>
                            <input @blur="check_username" v-model="username" type="text" name="username" id="user_name">
                            <span v-show="error_name" class="error_tip">{{ error_name_message }}</span>
                        </li>
                        <li>
                            <label>密码:</label>
                            <input v-model="password" @blur="check_pwd" type="password" name="password" id="pwd">
                            <span v-show="error_password" class="error_tip">请输入8-20位的密码</span>
                        </li>
                        <li>
                            <label>确认密码:</label>
                            <input @blur="check_cpwd" v-model="password2" type="password" name="password2" id="cpwd">
                            <span v-show="error_check_password" class="error_tip">两次输入的密码不一致</span>
                        </li>
                        <li>
                            <label>手机号:</label>
                            <input @blur="check_phone" v-model="mobile" type="text" name="mobile" id="phone">
                            <span v-show="error_phone" class="error_tip">请输入正确的手机号码</span>
                        </li>
                        <li>
                            <label>图形验证码:</label>
                            <input type="text" v-model="image_code" @blur="check_image_code" name="image_code"
                                   id="pic_code" class="msg_input">
                            <img :src="image_code_url" @click="generate_image_code" alt="图形验证码" class="pic_code">
                            <span v-show="error_image_code" class="error_tip">{{ error_image_code_message }}</span>
                        </li>
                        <li>
                            <label>短信验证码:</label>
                            <input type="text" v-model="sms_code" @blur="check_sms_code" name="sms_code" id="msg_code"
                                   class="msg_input">
                            <a @click="send_sms_code" class="get_msg_code">{{ sms_code_tip }}</a>
                            <span class="error_tip" v-show="error_sms_code">{{ error_sms_code_message }}</span>
                        </li>
                        <li class="agreement">
                            <input v-model="allow" type="checkbox" name="allow" id="allow" >
                            <label>同意”美多商城用户使用协议“</label>
                            <span v-show="error_allow" class="error_tip">请勾选用户协议</span>
                        </li>
                        <li class="reg_sub">
                            <input type="submit" value="注 册">
                        </li>
                    </ul>
                </form>
            </div>
        </div>
    </div>

    <div class="footer no-mp">
        <div class="foot_link">
            <a href="#">关于我们</a>
            <span>|</span>
            <a href="#">联系我们</a>
            <span>|</span>
            <a href="#">招聘人才</a>
            <span>|</span>
            <a href="#">友情链接</a>
        </div>
        <p>CopyRight © 2016 北京美多商业股份有限公司 All Rights Reserved</p>
        <p>电话：010-****888    京ICP备*******8号</p>
    </div>
    <script type="text/javascript" src="js/common.js"></script>
    <script type="text/javascript" src="js/register.js"></script>
</body>
</html>
```

register.js  文件: 

```js
var vm = new Vue({
    el: '#app',
    data: {
        host: host,

        error_name: false,
        error_password: false,
        error_check_password: false,
        error_phone: false,
        error_allow: false,
        error_sms_code: false,
        error_name_message: '',
        error_phone_message: '',
        error_sms_code_message: '',
        error_image_code:'',

        sms_code_tip: '获取短信验证码',
        sending_flag: false, // 正在发送短信标志

        // 图形验证码:
        image_code_id: '',
        image_code_url: '',

        username: '',
        password: '',
        password2: '',
        mobile: '',
        sms_code: '',
        allow: false,
        image_code:'',
        error_image_code_message:''
    },
    mounted: function(){
		// 向服务器获取图片验证码
		this.generate_image_code();
	},
    methods: {
        // 生成一个图片验证码的编号，并设置页面中图片验证码img标签的src属性
		generate_image_code: function(){
			// 生成一个编号 : 严格一点的使用uuid保证编号唯一， 不是很严谨的情况下，也可以使用时间戳
			this.image_code_id = generateUUID();
			// 设置页面中图片验证码img标签的src属性
			this.image_code_url = this.host + "/image_codes/" + this.image_code_id + "/";
		},
        // 检查用户名
        check_username: function () {
            var re = /^[a-zA-Z0-9_-]{5,20}$/;
            if (re.test(this.username)) {
                this.error_name = false;
            } else {
                this.error_name_message = '请输入5-20个字符的用户名';
                this.error_name = true;
            }
            // 检查重名
            if (this.error_name == false) {
                var url = this.host + '/usernames/' + this.username + '/count/';
                axios.get(url, {
                    responseType: 'json'
                })
                    .then(response => {
                        if (response.data.count > 0) {
                            this.error_name_message = '用户名已存在';
                            this.error_name = true;
                        } else {
                            this.error_name = false;
                        }
                    })
                    .catch(error => {
                        console.log(error.response);
                    })
            }
        },
        check_pwd: function () {
            var len = this.password.length;
            if (len < 8 || len > 20) {
                this.error_password = true;
            } else {
                this.error_password = false;
            }
        },
        check_cpwd: function () {
            if (this.password != this.password2) {
                this.error_check_password = true;
            } else {
                this.error_check_password = false;
            }
        },
        // 检查手机号
        check_phone: function () {
            var re = /^1[345789]\d{9}$/;
            if (re.test(this.mobile)) {
                this.error_phone = false;
            } else {
                this.error_phone_message = '您输入的手机号格式不正确';
                this.error_phone = true;
            }
            if (this.error_phone == false) {
                var url = this.host + '/mobiles/' + this.mobile + '/count/';
                axios.get(url, {
                    responseType: 'json'
                })
                    .then(response => {
                        if (response.data.count > 0) {
                            this.error_phone_message = '手机号已存在';
                            this.error_phone = true;
                        } else {
                            this.error_phone = false;
                        }
                    })
                    .catch(error => {
                        console.log(error.response);
                    })
            }
        },
        // 检查图片验证码
		check_image_code: function (){
			if(!this.image_code) {
				this.error_image_code_message = '请填写图片验证码';
				this.error_image_code = true;
			} else {
				this.error_image_code = false;
			}
		},
        check_sms_code: function () {
            if (!this.sms_code) {
                this.error_sms_code_message = '请填写短信验证码';
                this.error_sms_code = true;
            } else {
                this.error_sms_code = false;
            }
        },
        check_allow: function () {
            if (!this.allow) {
                this.error_allow = true;
            } else {
                this.error_allow = false;
            }
        },
        // 发送手机短信验证码
        send_sms_code: function () {
            if (this.sending_flag == true) {
                return;
            }
            this.sending_flag = true;

            // 校验参数，保证输入框有数据填写
            this.check_phone();

            if (this.error_phone == true) {
                this.sending_flag = false;
                return;
            }

            // 向后端接口发送请求，让后端发送短信验证码
            var url = this.host + '/sms_codes/' + this.mobile + '/' + '?image_code=' + this.image_code
                + '&image_code_id=' + this.image_code_id
            axios.get(url, {
                responseType: 'json'
            })
                .then(response => {
                    // 表示后端发送短信成功
                    // 倒计时60秒，60秒后允许用户再次点击发送短信验证码的按钮
                    var num = 60;
                    // 设置一个计时器
                    var t = setInterval(() => {
                        if (num == 1) {
                            // 如果计时器到最后, 清除计时器对象
                            clearInterval(t);
                            // 将点击获取验证码的按钮展示的文本回复成原始文本
                            this.sms_code_tip = '获取短信验证码';
                            // 将点击按钮的onclick事件函数恢复回去
                            this.sending_flag = false;
                        } else {
                            num -= 1;
                            // 展示倒计时信息
                            this.sms_code_tip = num + '秒';
                        }
                    }, 1000, 60)
                })
                .catch(error => {
                    if (error.response.status == 400) {
                        this.error_sms_code_message = error.response.data.message;
                        this.error_sms_code = true;
                    } else {
                        console.log(error.response.data);
                    }
                    this.sending_flag = false;
                })
        },
        // 注册
        on_submit: function () {
            this.check_username();
            this.check_pwd();
            this.check_cpwd();
            this.check_phone();
            this.check_sms_code();
            this.check_allow();

            // if(this.error_name == false && this.error_password == false && this.error_check_password == false
            //     && this.error_phone == false && this.error_sms_code == false && this.error_allow == false) {
            //     var url = this.host + '/users/';
            //     axios({
            //       url:url,
            //       method: 'post',
            //       data: {
            //         username: this.username,
            //         password: this.password,
            //         password2: this.password2,
            //         mobile: this.mobile,
            //         sms_code: this.sms_code,
            //         allow: this.allow.toString()
            //       }, headers: {
            //         responseType: 'json'
            //       }})
            //         .then(response => {
            //             location.href = '/index.html';
            //         })
            //         .catch(error=> {
            //             if (error.response.status == 400) {
            //                 if ('non_field_errors' in error.response.data) {
            //                     this.error_sms_code_message = error.response.data.non_field_errors[0];
            //                 } else {
            //                     this.error_sms_code_message = '数据有误';
            //                 }
            //                 this.error_sms_code = true;
            //             } else {
            //                 console.log(error.response.data);
            //             }
            //         })
            //   }

            // 点击注册按钮之后, 发送请求 (下面的代码是通过请求体传参的)
            if (this.error_name == false && this.error_password == false && this.error_check_password == false
                && this.error_phone == false && this.error_sms_code == false && this.error_allow == false) {
                axios.post(this.host + '/users/', {
                    username: this.username,
                    password: this.password,
                    password2: this.password2,
                    mobile: this.mobile,
                    sms_code: this.sms_code,
                    allow: this.allow.toString()
                }, {
                    responseType: 'json',
                    withCredentials:true
                })
                    .then(response => {
                        if (response.data.code==0) {
                           location.href = 'index.html';
                        }
                    })
                    .catch(error => {
                        if (error.response.status == 400) {
                            if ('non_field_errors' in error.response.data) {
                                this.error_sms_code_message = error.response.data.non_field_errors[0];
                            } else {
                                this.error_sms_code_message = '数据有误';
                            }
                            this.error_sms_code = true;
                        } else {
                            console.log(error.response.data);
                        }
                    })
            }
        }
    }
});
```












