<template>
<div id="container">
  <div id="left">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="案例名称">
        <el-input v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item label="业务模块">
        <el-radio-group class="radiogroup" v-model="form.module">
          <el-radio label="融资融券交易"></el-radio>
          <el-radio label="融资融券管理"></el-radio>
          <el-radio label="股票质押"></el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="版本信息">
        <el-input v-model="form.version"></el-input>
      </el-form-item>
      <el-form-item label="专题名称">
        <el-input v-model="form.pkg"></el-input>
      </el-form-item>
      <el-form-item label="jira号1">
        <el-input placeholder="" v-model="form.jira1" class="input-with-select">
          <el-select v-model="form.jira1_select" slot="prepend" placeholder="">
            <el-option label="SECREQ" value="1"></el-option>
            <el-option label="SECGPZY" value="2"></el-option>
            <el-option label="SECRZRQ" value="3"></el-option>
          </el-select>
        </el-input>
      </el-form-item>
      <el-form-item label="jira号2" v-model='form.jira2'>
        <el-input v-model="form.jira2"><template slot="prepend">SECTEST</template></el-input>
      </el-form-item>
      <el-form-item label="提交人">
        <el-input v-model="form.author"></el-input>
      </el-form-item>
      <el-form-item label="提交日期">
        <el-date-picker type="date" value-format="yyyyMMdd" placeholder="请选择日期" v-model="form.date" style="width: 100%;"></el-date-picker>
      </el-form-item>
      <el-form-item label="备注信息">
        <el-input type="textarea" v-model="form.note"></el-input>
      </el-form-item>
      <el-form-item label="选择模板">
        <el-radio-group class="radiogroup" v-model="form.template">
          <el-radio label="前台"></el-radio>
          <el-radio label="testapp"></el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="init_tc()">创建案例</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</div>
</template>

<script>
  import querystring from 'querystring';
  export default {
    data() {
      return {
        form: { 
          api: 'tc_info',
          title: '',
          module: '',
          version: '',
          pkg: '',
          jira1: '',
          jira1_select: '1',
          jira2: 'xxxx',
          author: '钱秋实',
          date: '',
          template: '',
          note: ''
        }
      };
    },
    methods: {
      init_tc() {
        var data = querystring.stringify(this.form);
        console.log(data);
        this.$http.post('http://127.0.0.1:5000/api', data).then(function (response) {
          console.log(response);
        }).catch(function (error) {
          console.log(error);
        });
      }
    }
  }
</script>

<style>
body {
  overflow: scroll;
  font-size: 14px;
}
#left {
  width: 37%;
  float: left;
  margin-top: 0;
}
#right {
  position: relative;
  margin-left: 40%;
}
#right-top {
  height: 44px;
}
#right-bottom {
  margin-top:20px;
}
el-form {
  size: small;
}
.el-input {
  size: small;
}
.el-input__inner {
  margin-top: 0;
}
.radiogroup {
  text-align: left;
}
.el-select {
  width: 105px;
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  };
  align: middle;
}
.el-col {
  border-radius: 4px;
}
.tc_title__inner {
  vertical-align: middle;
  display: inline-block;
  height: 44px;
  text-align: center;
  line-height: 44px;
}
.tc_steps {
  height: 44px;
  margin-top: 10px;
}
.tc_submit {
  position: relative;
  margin-bottom: 300px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>