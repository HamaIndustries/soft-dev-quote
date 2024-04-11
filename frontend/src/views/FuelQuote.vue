<script scoped>
import SubmitButton from '@/components/SubmitButton.vue';

export default {
  name: 'FuelQuote',
  data() {
    return {
      form: {
        gallons: null,
        address: 'Texas',
        delivery: ''
      },
      price: '',
      amount: ''
    }
  },
  watch: {
    'form.gallons': function (newVal) {
      this.calculate()
    }
  },
  methods: {
    getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    },
    calculate() {
      if (this.form.gallons == null || this.form.gallons === '') {
        this.price = ''
        this.amount = ''
      } else {
        const unit_price = 10
        const total_price = this.form.gallons * unit_price
        this.price = `$${unit_price}`
        this.amount = `$${total_price}`
      }
    },
    onSubmit() {
      fetch('http://127.0.0.1:8000/api/pricing/fuelquote/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': this.getCookie('csrftoken')
        },
        body: JSON.stringify({
          gallons_requested: this.form.gallons,
          delivery_address: this.form.address,
          delivery_date: this.form.delivery,
          suggested_price_per_gallon: parseFloat(this.price.replace('$', '')),
          total_amount_due: parseFloat(this.amount.replace('$', ''))
        })
      })
      .then(response => {
        if(response.ok) {
          return response.json();
        }
        throw new Error('Network response was not ok.');
      })
      .then(data => {
        console.log(data);
        this.$router.push({ 
          path: 'quotehistory',
          query: {
            gallons: this.form.gallons,
            address: this.form.address,
            delivery: this.form.delivery,
            price: parseFloat(this.price.replace('$', '')),
            amount: parseFloat(this.amount.replace('$', ''))
          } 
        });
      })
      .catch(error => console.error('Error:', error));
    },
    checkHistory() {
      this.$router.push({ path: 'quotehistory' })
    }
  },
  components: {
    SubmitButton
  }
}
</script>

<template>
<div class="container">
    <h2>Fuel Quote</h2>
    <form @submit.prevent="onSubmit">
      <div class="group">
        <label for="gallons">Gallons Requested</label>
        <input type="number" id="gallons" v-model.number="form.gallons" required />
      </div>
      <div class="group">
        <label for="address">Delivery Address</label>
        <input type="text" id="address" v-model="form.address" readonly />
      </div>
      <div class="group">
        <label for="delivery">Delivery Date</label>
        <input type="date" id="delivery" v-model="form.delivery" required />
      </div>
      <div class="group">
        <label for="price">Suggested Price</label>
        <input type="text" id="price" v-model="price" readonly />
      </div>
      <div class="group">
        <label for="amount">Total Amount Due</label>
        <input type="text" id="amount" v-model="amount" readonly />
      </div>
      <div class="group separated">
        <SubmitButton type="submit">Get Quote</SubmitButton>
        <SubmitButton @click="checkHistory">Check History</SubmitButton>
      </div>
    </form>
  </div>
</template>

<style>

.container {
  color: #333;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  margin-top: 5%;
  margin-bottom: 5%;
  width: 340px;
  background: #ffffff;
  padding: 40px;
  border-radius: 8px;
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.group {
  margin-bottom: 20px;
  transition: all 0.3s ease;
}

.group label {
  display: block;
  margin-bottom: 10px;
  font-size: 14px;
  font-weight: 600;
  color: #555;
  transition: all 0.3s ease;
}

.group input {
  width: 100%;
  border: 1px solid #cfd8dc;
  border-radius: 6px;
  font-size: 14px;
  background-color: #f7f7f7;
  color: #333;
  transition:
    border-color 0.3s ease,
    background-color 0.3s ease;
}

.group input:focus {
  outline: none;
  border-color: #5c6bc0;
  background-color: #ffffff;
}

.group button {
  width: 40%;
  padding: 15px;
  border: none;
  background-image: linear-gradient(135deg, #03551b 10%, #16d21f 90%);
  color: white;
  font-size: 16px;
  border-radius: 6px;
  cursor: pointer;
  transition: background-image 0.3s ease;
}


.group.separated {
  display: flex;
  justify-content: space-between;
}

.group button:hover {
  background-image: linear-gradient(135deg, #2c2c2c 10%, #878787 90%);
}

form {
  width: 100%;
}

@media (min-width: 1024px) {
  .container {
    width: 60%;
  }
}

</style>
