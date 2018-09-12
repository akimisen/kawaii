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
        <el-button type="primary" @click="onSubmit">创建案例</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
  <div></div>
  <div id="right">
    <div id="right-top">
      <el-row :gutter="10" class="tc_title">
        <el-col :span="2"><div class="grid-content bg-purple"><div class="tc_title__inner">Step</div></div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple"><div class="tc_title__inner">Content</div></div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple"><div class="tc_title__inner">Expected Result</div></div></el-col>
        <el-col :span="6"><div class="grid-content bg-purple"><div class="tc_title__inner">Actual Result</div></div></el-col>
        <el-col :span="2"><div class="grid-content bg-purple"><div class="tc_title__inner">Pass</div></div></el-col>
      </el-row>
    </div>
    <div id="right-bottom">
      <el-form :model="dynamicValidateForm" ref="dynamicValidateForm" label-width="0" class="demo-dynamic">
        <el-form-item
          v-for="(step, index) in dynamicValidateForm.steps"
          class="tc_steps"
          label=""
        >
          <el-row :gutter="10" class="tc_step__row"> 
            <el-col :span="2"><div class="grid-content bg-purple tc_step__input tc_step__index" v-text="index+1"></div></el-col>
            <el-col :span="6"><div class="tc_step__input"><el-input type="textarea" class="tc_step_textarea" v-model="step.content" placeholder="测试过程"></el-input></div></el-col> 
            <el-col :span="6"><div class="tc_step__input"><el-input type="textarea" class="tc_step_textarea" v-model="step.res1" placeholder="预期输出"></el-input></div></el-col> 
            <el-col :span="6"><div class="tc_step__input"><el-input type="textarea" class="tc_step_textarea" v-model="step.res2" placeholder="实际输出"></el-input></div></el-col> 
            <el-col :span="2"><div class="tc_step__input"><el-switch class="tc_step_pass" v-model="step.pass"></el-switch></div></el-col> 
            <el-col :span="2"><div class="tc_step__button"><el-button type="primary" @click.prevent="removeStep(step)">删除</el-button></div></el-col>
          </el-row>
        </el-form-item>
        <el-form-item class="tc_submit">
          <el-button type="primary" @click="submitForm('dynamicValidateForm')">提交</el-button>
          <el-button @click="addStep">新增</el-button>
          <el-button @click="resetForm('dynamicValidateForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</div>
</template>

<script>
  export default {
    data() {
      return {
        form: {
          title: '',
          module: '',
          version: '',
          pkg: '',
          jira1: '',
          jira1_select: '1',
          jira2: '',
          author: '钱秋实',
          date: '',
          template: '',
          note: ''
        },
        dynamicValidateForm: {
          title: '',
          module: '',
          version: '',
          pkg: '',
          author: '',
          date: '',
          steps: [{
            content: '', res1: '', res2: '', pass: true
          }]
        }
      };
    },
    methods: {
      onSubmit() {
        var data = JSON.stringify(this.form);
        console.log(data);
        this.$http.post('http://127.0.0.1:5000/test', data, {"emulateJSON":true}).then((response) => {
          // successful callback
          console.log('succeed!');
        }, (response) => {
          // failure callback
          console.log('oops...');
        })
      },
      submitForm(formName) {
        this.dynamicValidateForm.title = this.form.title;
        this.dynamicValidateForm.module = this.form.module;
        this.dynamicValidateForm.version = this.form.version;
        this.dynamicValidateForm.author = this.form.author;
        this.dynamicValidateForm.date = this.form.date;
        this.dynamicValidateForm.pkg = this.form.pkg;
        var tc_data= JSON.stringify(this.dynamicValidateForm);
        console.log(tc_data);
        this.$http.post('http://127.0.0.1:5000/test', tc_data, {"emulateJSON":true}).then((response) => {
          // success
          console.log('succeeded!');
        }, (response) => {
          // failure
          console.log('oops...something went wrong.');
        })
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      removeStep(item) {
        var index = this.dynamicValidateForm.steps.indexOf(item)
        if (index !== -1) {
          this.dynamicValidateForm.steps.splice(index, 1)
        }
      },
      addStep() {
        this.dynamicValidateForm.steps.push({
          content: '',
          res1 : '',
          res2 : '',
          pass : true
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
  font-size: 14px;
}
#left {
  width: 37%;
  float: left;
  font-size :8px;
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