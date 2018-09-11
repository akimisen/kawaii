<template>
<div id="container">
  <div id="left">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="案例名称">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="业务模块">
        <el-radio-group class="radiogroup" v-model="form.module">
          <el-radio label="融资融券交易"></el-radio>
          <el-radio label="融资融券管理"></el-radio>
          <el-radio label="股票质押"></el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="专题名称">
        <el-input v-model="form.theme"></el-input>
      </el-form-item>
      <el-form-item label="版本信息">
        <el-input v-model="form.version"></el-input>
      </el-form-item>
      <el-form-item label="jira号1" v-model='form.jira1'>
        <el-input v-model="form.jira1"><template slot="prepend">SECREQ -</template></el-input>
      </el-form-item>
      <el-form-item label="jira号2" v-model='form.jira2'>
        <el-input v-model="form.jira2"><template slot="prepend">SECTEST-</template></el-input>
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
        <el-button type="primary" @click="onSubmit">创建案例</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
  <div></div>
  <div id="right"></div>
</div>
</template>
<script>
  export default {
    data() {
      return {
        form: {
          name: '',
          module: '',
          theme: '',
          version: '',
          jira1: '',
          jira2: '',
          author: '钱秋实',
          date: '',
          template: '',
          note: ''
        }
      };
    },
    methods: {
      onSubmit() {
        var data = JSON.stringify(this.form);
        this.$http.post('/test/', data).then((response) => {
          // success callback
        }, (response) => {
          console.log('oops...')
        });
      },
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>
<style>
body {
  overflow: hidden;
}
div {
  width: 360px;
}
el-form {
  size: small;
}
.radiogroup {
  text-align: left
}
</style>