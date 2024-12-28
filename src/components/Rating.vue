<template>
  <div class="circle-wrapper">
    <div class="circle">
      <svg width="150" height="150" viewBox="0 0 150 150">
        <!-- Background Circle -->
        <circle cx="75" cy="75" r="70" stroke="#e5e5e5" stroke-width="15" fill="none" />
        <!-- Progress Circle -->
        <circle
          :stroke-dashoffset="progressOffset"
          cx="75"
          cy="75"
          r="70"
          stroke="#4caf50"
          stroke-width="15"
          stroke-dasharray="440"
          fill="none"
        />
      </svg>
      <div class="percentage-text" v-if="outputPercentage !== null">
        <p>{{ outputPercentage }}%</p>
      </div>
    </div>
  </div>
  <div>{{ source }}</div>
</template>

<script>
export default {
  name: 'MovieRating',
  props: {
    values: {
      type: String,
      required: true,
    },
    source: {
      type: String,
      default: '', // Optional prop for source
    },
  },
  data() {
    return {
      outputPercentage: null, // The result after conversion
    };
  },
  computed: {
    // Compute the dash offset based on the percentage value
    progressOffset() {
      const strokeLength = 440; // Circumference of the circle (2 * π * radius)
      if (this.outputPercentage !== null) {
        return strokeLength - (strokeLength * (this.outputPercentage / 100)); // Calculate offset
      }
      return strokeLength; // Default offset (full circle)
    },
  },
  watch: {
    // Watch for changes in values prop and recalculate the percentage
    values: 'convertToPercentage',
  },
  methods: {
    // Convert the input value to a percentage
    convertToPercentage() {
      const value = this.values.trim();

      // Regex to match ratio like 7.6/10
      const ratioPattern = /^(\d+(\.\d+)?)\/(\d+(\.\d+)?)$/;
      
      // Regex to match percentage like 86%
      const percentagePattern = /^(\d+(\.\d+)?)%$/;

      let percentage;

      // Check if the input matches a ratio (e.g., '7.6/10')
      if (ratioPattern.test(value)) {
        const match = value.match(ratioPattern);
        const numerator = parseFloat(match[1]);
        const denominator = parseFloat(match[3]);
        percentage = (numerator / denominator) * 100; // Convert ratio to percentage
      }
      // Check if the input is already a percentage (e.g., '86%')
      else if (percentagePattern.test(value)) {
        const match = value.match(percentagePattern);
        percentage = parseFloat(match[1]); // Extract numeric value from percentage
      }
      // Check if the input matches a fraction like '76/100'
      else if (value.includes('/')) {
        const parts = value.split('/');
        const numerator = parseFloat(parts[0]);
        const denominator = parseFloat(parts[1]);
        percentage = (numerator / denominator) * 100;
      } 
      // Invalid input format
      else {
        this.outputPercentage = 'Invalid input format. Please use either ratio, fraction or percentage format.';
        return;
      }

      // Update the output percentage to 2 decimal places
      this.outputPercentage = parseFloat(percentage.toFixed(2)); 
    },
  },
  mounted() {
    // Initially convert input value when the component mounts
    this.convertToPercentage();
  },
};
</script>

<style scoped>
svg{
  height: 50px;
  width: 50px;
}
.circle-wrapper {
  position: relative;
  width: 50px;
  height: 50px;
  background: #f3f3f3;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.circle {
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 50%;
}

.circle svg {
  position: absolute;
  transform: rotate(-90deg); /* Start the circle from top */
}

.circle-wrapper .percentage-text {
  font-size: 12px;
  font-weight: bold;
  color: #333;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
}
</style>
