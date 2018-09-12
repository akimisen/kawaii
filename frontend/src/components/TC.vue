<template>
<div id="container">
  <div id="tc">
    <el-row :gutter="10" class="tc_title_row">
      <el-col :span="2"><div class="grid_content bg_purple"><div class="tc_title_inner">Step</div></div></el-col>
      <el-col :span="6"><div class="grid_content bg_purple"><div class="tc_title_inner">Content</div></div></el-col>
      <el-col :span="6"><div class="grid_content bg_purple"><div class="tc_title_inner">Expected Result</div></div></el-col>
      <el-col :span="6"><div class="grid_content bg_purple"><div class="tc_title_inner">Actual Result</div></div></el-col>
      <el-col :span="2"><div class="grid_content bg_purple"><div class="tc_title_inner">Pass</div></div></el-col>
    </el-row>
  </div>
  <div id="right-bottom">
    <el-form :model="dynamic_tc_form" ref="dynamic_tc_form" label-width="0" class="tc_form">
      <el-form-item
        v-for="(step, index) in dynamic_tc_form.steps"
        class="tc_form_item"
        label=""
      >
        <el-row :gutter="10" class="tc_step_row">
          <el-col :span="2"><div class="grid_content bg_purple tc_step_input tc_step_index" v-text="index+1"></div></el-col>
          <el-col :span="6"><div class="tc_step_input"><el-input type="textarea" class="tc_step_textarea" v-model="step.content" placeholder="测试过程"></el-input></div></el-col>
          <el-col :span="6"><div class="tc_step_input"><el-input type="textarea" class="tc_step_textarea" v-model="step.res1" placeholder="预期输出"></el-input></div></el-col>
          <el-col :span="6"><div class="tc_step_input"><el-input type="textarea" class="tc_step_textarea" v-model="step.res2" placeholder="实际输出"></el-input></div></el-col>
          <el-col :span="2"><div class="tc_step_input"><el-switch class="tc_step_pass" v-model="step.pass"></el-switch></div></el-col>
          <el-col :span="2"><div class="tc_step_button"><el-button type="primary" @click.prevent="removeStep(step)">删除</el-button></div></el-col>
          <div class="clearfloat"></div>
        </el-row>
      </el-form-item>
      <el-form-item class="tc_submit">
        <el-button type="primary" @click="submitForm('dynamic_tc_form')">提交</el-button>
        <el-button @click="addStep">新增</el-button>
        <el-button @click="resetForm('dynamic_tc_form')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</div>
</template>

<script>
  export default {
    data() {
      return {
        dynamic_tc_form: {
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
        this.$http.post('http://127.0.0.1:5000/test', data).then(function (response) {
          console.log(response);
        }).catch(function (error) {
          console.log(error);
        });
      },
      submitForm(formName) {
        this.dynamic_tc_form.title = this.form.title;
        this.dynamic_tc_form.module = this.form.module;
        this.dynamic_tc_form.version = this.form.version;
        this.dynamic_tc_form.author = this.form.author;
        this.dynamic_tc_form.date = this.form.date;
        this.dynamic_tc_form.pkg = this.form.pkg;
        var tc_data= JSON.stringify(this.dynamic_tc_form);
        console.log(tc_data);
        this.$http.post('http://127.0.0.1:5000/test', tc_data).then(function (response) {
          console.log(response);
        }).catch(function (error) {
          console.log(error);
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      removeStep(item) {
        var index = this.dynamic_tc_form.steps.indexOf(item)
        if (index !== -1) {
          this.dynamic_tc_form.steps.splice(index, 1)
        }
      },
      addStep() {
        this.dynamic_tc_form.steps.push({
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
.tc_title_inner {
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
.clearfloat {
  clear:both;height:0;font-size: 1px;line-height: 0px;
}
.bg_purple_dark {
  background: #99a9bf;
}
.bg_purple {
  background: #d3dce6;
}
.bg_purple_light {
  background: #e5e9f2;
}
.grid_content {
  border-radius: 4px;
  min-height: 36px;
}
.row_bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
