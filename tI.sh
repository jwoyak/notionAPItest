curl 'https://api.notion.com/v1/blocks/44618b323eb84762bed36343ea4b5caa/children?page_size=100' \
  -H 'Authorization: Bearer '"$NOTION_KEY"'' \
  -H "Notion-Version: 2022-06-28"
