<template>
    <v-flex>
        <v-container>
            <v-card>
                <v-data-table
                :headers="headers"
                :items="users"
                :pagination.sync="pagination"
                class="elevation-1"
                hide-actions
                no-data-text="データが存在しません"
                >
                    <template slot="items" slot-scope="props">
                    <td class="text-xs-left">{{ props.item.name }}</td>
                    <td class="text-xs-left">{{ props.item.email }}</td>
                    <td class="text-xs-left">{{ props.item.description }}</td>
                    <td class="text-xs-left">{{ props.item.website }}</td>
                    </template>
                </v-data-table>
            </v-card>
        </v-container>
        <div class="text-xs-center">
            <v-pagination 
            v-model="pagination.page" 
            :length="pages"></v-pagination>
        </div>
    </v-flex>
</template>

<script>
  export default {
    created() {
      this.getUsers()
    },
    data () {
      return {
        search: '',
        pagination: {
            rowsPerPage: 1
        },
        selected: [],
        headers: [
          {
            text: 'Name',
            align: 'left',
            // sortable: false,
            value: 'name'
          },
					{ text: 'Email',
						align: 'left',
					 	value: 'email' },
					{ text: 'Description',
						align: 'left',
						value: 'description' },
					{ text: 'Website', 
						align: 'left',
						value: 'website' }
        ]
      }
    },
    computed: {
			users() {
				return this.$store.getters.getUsers
			},
      pages() {
        return this.$store.getters.getPages
      },
    },
    methods: {
			getUsers(){
				this.$store.dispatch('getUsersAction', this.pagination.rowsPerPage)
			}
    }
  }
</script>