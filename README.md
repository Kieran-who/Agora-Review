# The Agora Review

The Agora Review is an experiment in AI discourse. Each week, we host a roundtable discussion on a new topic, featuring AI-generated personas taking on the role of leading thinkers from various related fields. Our goal is to test how well we can explore complex issues through diverse _(AI)_ perspectives.

Each roundtable is based around a provided academic paper, which the participants read and discuss. The discussion is moderated by a host persona, who steers the conversation and ensures all voices are heard. After the discussion, a detailed summary of the key points and insights from the debate are generated. This summary and the full transcript of the discussion are then published on this site.

The Agora Review is built using a custom pipeline that leverages large language models to generate the personas, moderate the discussion, and produce the write-up. The full code for the project is open source and available on [GitHub](https://github.com/Kieran-who/Agora-Review)

If you have any feedback or suggestions for future topics, please get in touch via [email](mailto:kieran@transparency-project.ai)

## Running the Code:

This is currently only configured to run with Azure OpenAI, Google Gemini and Mistral for document OCR. You will need access to all services to run the code. This was just a quick proof of concept so no plans to develop it any further but open to PRs to add support for direct OpenAI support.

Create an .env file in the root directory with the following variables:

```
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_RESOURCE_NAME=
AZURE_OPENAI_SMALL_DEPLOYMENT_NAME=
AZURE_OPENAI_LARGE_DEPLOYMENT_NAME=

GOOGLE_LARGE_MODEL_NAME="gemini-2.5-pro-preview-06-05"
GOOGLE_SMALL_MODEL_NAME="gemini-2.5-flash"
GOOGLE_API_KEY=

MISTRAL_API_KEY=
```

Then run the following command, replacing `path_to_paper.pdf` with the path to your PDF file to kick off a new roundtable discussion:

```
python src/main.py path_to_paper.pdf
```

### Publishing

The code is currently configured to automatically published content to a Cloudflare pages site using Vitepress.
