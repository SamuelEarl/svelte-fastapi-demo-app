<main>
  <form on:submit|preventDefault={handleSubmit}>
    <select bind:value={formData.framework}>
      <option value="">-- What is your favorite framework? --</option>
      <option value="svelte">Svelte</option>
      <option value="vue">Vue</option>
      <option value="react">React</option>
      <option value="other">Other</option>
    </select>

    <br><br>

    <button type="submit">Submit Form</button>
    <button type="reset">Reset Form</button>
  </form>

  <div>Your selection: { formData.framework }</div>
  <div>The server response: { serverResponse }</div>

  <!-- <img src={logo} alt="Svelte Logo" />
  <h1>Hello world!</h1>

  <Counter id="0" />

  <p>
    Visit <a href="https://svelte.dev">svelte.dev</a> to learn how to build Svelte
    apps.
  </p>

  <p>
    Check out <a href="https://github.com/sveltejs/kit#readme">SvelteKit</a> for
    the officially supported framework, also powered by Vite!
  </p> -->
</main>

<script>
  import logo from "./assets/svelte.png";
  import Counter from "./lib/Counter.svelte";

  let formData = {
    framework: ""
  };

  let serverResponse = "";

  async function handleSubmit() {
    try {
      const response = await fetch("/api/submit-framework", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });
      if (response.ok) {
        let result = await response.json();
        console.log("RESULT:", result);
        serverResponse = result.message;
      }
      else {
        console.log("Submission Error:", response.status);
      }      
    }
    catch(err) {
      console.log("ERROR:", err);
    }
  }
</script>

<style>
  :root {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
      Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  }

  main {
    text-align: center;
    padding: 1em;
    margin: 0 auto;
  }

  img {
    height: 16rem;
    width: 16rem;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4rem;
    font-weight: 100;
    line-height: 1.1;
    margin: 2rem auto;
    max-width: 14rem;
  }

  p {
    max-width: 14rem;
    margin: 1rem auto;
    line-height: 1.35;
  }

  @media (min-width: 480px) {
    h1 {
      max-width: none;
    }

    p {
      max-width: none;
    }
  }
</style>
