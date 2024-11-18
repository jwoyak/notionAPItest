const { Client } = require(['@notionhq/client'], function (client) {
});

const notion = new Client({ auth: process.env.NOTION_API_KEY })

const databaseId = 'be41a5768e3b45f0b9525e1ce974cf75'

// ----------------------------------------------------
// Add a database item
async function addItem(text) {
  try {
    const response = await notion.pages.create({
      parent: { database_id: databaseId },
      properties: {
        title: {
          title:[
            {
              "text": {
                "content": text
              }
            }
          ]
        }
      },
    })
    console.log(response)
    console.log("Success! Entry added.")
  } catch (error) {
    console.error(error.body)
  }
}
//addItem("Yurts in Big Sur, California")
// ----------------------------------------------------


// Query database item
async function getDone() {
    const response = await notion.databases.query({
      database_id: databaseId,
        "filter": {
          "property": "Done",
          "checkbox": {
            "equals": true
          }
        }
    })
    console.log(response)
    document.getElementById('ToDo').innerHTML = response;
  }
getDone()